import pytest

from game import Game

@pytest.fixture
def game()->Game:
    return Game()

def assert_ilegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


def test_exception_when_invalid_test(game):
    assert_ilegal_argument(game,None)
    assert_ilegal_argument(game, "12")
    assert_ilegal_argument(game, "1234")
    assert_ilegal_argument(game, "12s")
    assert_ilegal_argument(game, "121")



