import pytest

from game import Game
from game_result import GameResult


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

@pytest.mark.parametrize('invalid_input',[None,"12","1234","12s","121"])
def test_exception_when_invalid_input(game,invalid_input):
    assert_ilegal_argument(game,invalid_input)

def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

def test_return_solved_result_if_matched_number(game):
    game.question ='123'
    assert_matched_number(result = game.guess("123"),solved= True,strikes=3,balls=0)



def test_return_solved_result_if_unmatched_number(game):
    game.question = '123'
    assert_matched_number(result = game.guess('456'), solved= False,strikes= 0,balls= 0)


def test_return_2_strikes_0_balls(game):
    game.question = '123'
    assert_matched_number(result=game.guess("125"), solved=False, strikes= 2, balls=0)
    game.question = '234'
    assert_matched_number(result=game.guess("534"), solved=False, strikes=2, balls=0)
    game.question = '615'
    assert_matched_number(result=game.guess("695"), solved=False, strikes=2, balls=0)

def test_return_1_strike_2_balls(game):
    game.question = '123'
    assert_matched_number(result=game.guess("321"), solved=False, strikes=1, balls=2)
    game.question = '234'
    assert_matched_number(result=game.guess("243"), solved=False, strikes=1, balls=2)
    game.question = '615'
    assert_matched_number(result=game.guess("165"), solved=False, strikes=1, balls=2)