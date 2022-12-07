from celery import shared_task
from nerdvanapp.models import User, Games, PriceAlert


@shared_task
def test_celery():
    user = User.objects.get(id=1)
    game = Games.objects.get(id=16516)

    PriceAlert.objects.create(
        user=user,
        game=game,
        price=200
    )
