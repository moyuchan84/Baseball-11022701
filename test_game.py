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


def test_exception_when_input_is_none(game):

    with pytest.raises(TypeError):
        game.guess(None)


def test_exception_when_input_is_unmatched(game):
    assert_ilegal_argument(game, "12")
