from .models import BoardGame, OwnedGame

def register_game(user, boardgame):
    _, created = OwnedGame.objects.get_or_create(owner=user, game=boardgame)
    return created

def remove_game(ownedgame):
    ownedgame.delete()


