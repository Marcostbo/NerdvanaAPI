from celery import shared_task
from nerdvanapp.models import User, Games, PriceAlert
from nerdvanapp.methods.game_pricing import GamePricing


@shared_task
def test_celery():
    """ This task evaluates all the price alerts create
     and check if any store has a price above the defined value"""

    price_alerts = PriceAlert.objects.all().filter(is_resolved=False)
    stores_list = ['Americanas', 'Kabum']
    for price_alert in price_alerts:
        # evaluate the alert
        GamePricing().get_smaller_price_and_url_for_multiple_stores(
            game=price_alert.game.name,
            console='PS4',
            stores_list=stores_list
        )

    user = User.objects.get(id=1)
    game = Games.objects.get(id=16516)

    PriceAlert.objects.create(
        user=user,
        game=game,
        price=200
    )
