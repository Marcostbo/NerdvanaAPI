from celery import shared_task
from operator import itemgetter
from nerdvanapp.models import User, Games, PriceAlert, Store
from nerdvanapp.methods.game_pricing import GamePricing
from django.utils import timezone


@shared_task
def evaluate_price_alerts():
    """ This task evaluates all the price alerts create
     and check if any store has a price above the defined value"""

    price_alerts = PriceAlert.objects.all().filter(is_resolved=False)
    stores = Store.objects.all().values_list('search_name', 'link', 'name')
    for price_alert in price_alerts:
        # Evaluate if the alert is resolved
        game_prices = GamePricing().get_smaller_price_and_url_for_multiple_stores_v2(
            game=price_alert.game.name,
            console=price_alert.console,
            stores_list=stores
        )
        game_prices.sort(key=lambda x: (x['price'] is not None, x['price']), reverse=True)
        for game_price in game_prices:
            is_resolved = GamePricing().evaluate_price(
                price_limit=price_alert.price,
                current_price=game_price.get('price')
            ) if game_price.get('price') else False
            if is_resolved:
                # Mark price_alert as resolved
                price_alert.is_resolved = True
                price_alert.price_resolved = game_price.get('price')
                price_alert.link_resolved = game_price.get('url')
                price_alert.resolved_on = timezone.now()
                price_alert.save()
                # Send email to client about the resolved price alert
                GamePricing().send_email_price_alert_resolved(
                    user=price_alert.user,
                    game_name=price_alert.game.name,
                    price=game_price.get('price'),
                    link=game_price.get('url'),
                    store=game_price.get('store_name')
                )
                break
