from celery import shared_task
from nerdvanapp.models import User, Games, PriceAlert
from nerdvanapp.methods.game_pricing import GamePricing


def evaluate_price(price_limit: float, current_price: float):
    if current_price < price_limit:
        return True
    return False


@shared_task
def test_celery():
    """ This task evaluates all the price alerts create
     and check if any store has a price above the defined value"""

    price_alerts = PriceAlert.objects.all().filter(is_resolved=False)
    stores_list = ['Americanas', 'Kabum']
    for price_alert in price_alerts:
        # evaluate the alert
        game_prices = GamePricing().get_smaller_price_and_url_for_multiple_stores(
            game=price_alert.game.name,
            console='PS4',
            stores_list=stores_list
        )
        for game_price in game_prices:
            is_resolved = evaluate_price(
                price_limit=price_alert.price,
                current_price=game_price.get('price')
            )

    user = User.objects.get(id=1)
    game = Games.objects.get(id=16516)

    PriceAlert.objects.create(
        user=user,
        game=game,
        price=200
    )
