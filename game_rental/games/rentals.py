from .models import OwnedGame, BorrowedGame

class NoOwner(Exception):
    def __str__(self):
        return "Owned game has no owner!"

class GameAlreadyRentered(Exception):
    def __str__(self):
        return "Game is already being rented!"

class MustBeRentedToReturn(Exception):
    def __str__(self):
        return "The game cannot be returned since it is not rented!."


def initiate_deal(ownedgame, user):
    if not OwnedGame.owner:
        raise NoOwner

    if BorrowedGame.objects.filter(ownedgame=ownedgame, status='Rented'):
        raise GameAlreadyRented

    BorrowedGame(ownedgame=ownedgame, borrower=user).save()

def return_game(borrowedgame):
    if borrowedgame.status != 'Rented':
        raise MustBeRentedToReturn

    borrowedgame.update(status='Returned')

