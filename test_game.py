import pytest

from game import Game

@pytest.fixture
def game()->Game:
    return Game()

def assert_ilegal_argument(game, guessNumber):
    try:
        game.guess(guessNumber)
        pytest.fail()
    except TypeError:
        pass


def test_exception_when_invalid_test(game):
    assert_ilegal_argument(game,None)
    assert_ilegal_argument(game, "12")
    assert_ilegal_argument(game, "1234")



