from celery import shared_task
from operator import itemgetter
from nerdvanapp.models import User, Games, PriceAlert, Store
from nerdvanapp.methods.game_pricing import GamePricing
from django.utils import timezone


def evaluate_price(price_limit: float, current_price: float):
    if current_price < price_limit:
        return True
    return False


@shared_task
def evaluate_price_alerts():
    """ This task evaluates all the price alerts create
     and check if any store has a price above the defined value"""

    price_alerts = PriceAlert.objects.all().filter(is_resolved=False)
    stores = Store.objects.all().values_list('search_name', 'link', 'name')
    for price_alert in price_alerts:
        # Evaluate if the alert is resolved
        game_prices = GamePricing().get_smaller_price_and_url_for_multiple_stores(
            game=price_alert.game.name,
            console=price_alert.console,
            stores_list=stores
        )
        sorted_game_prices = sorted(game_prices, key=itemgetter('price'))
        for game_price in sorted_game_prices:
            is_resolved = evaluate_price(
                price_limit=price_alert.price,
                current_price=game_price.get('price')
            )
            if is_resolved:
                price_alert.is_resolved = True
                price_alert.price_resolved = game_price.get('price')
                price_alert.link_resolved = game_price.get('url')
                price_alert.resolved_on = timezone.now()
                price_alert.save()
                break
