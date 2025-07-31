from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self,value):
        self._question = value

    def guess(self, guess_number)->GameResult:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True,3,0)
        return None

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError('입력이 None입니다')
        if len(guess_number) != 3:
            raise TypeError('입력은 3자리 문자열이여야합니다.')
        if not guess_number.isdigit():
                raise TypeError('모든 문자는 숫자로 구성되어야 합니다.')
        if self.inDuplicatedNumber(guess_number):
            raise TypeError('중복된 숫자가 존재합니다')

    def inDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]