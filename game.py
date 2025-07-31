class Game:
    def guess(self, guessNumber):
        self._assert_illegal_value(guessNumber)

    def _assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError('입력이 None입니다')
        if len(guessNumber) != 3:
            raise TypeError('입력은 3자리 문자열이여야합니다.')
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError('모든 문자는 숫자로 구성되어야 합니다.')
        if self.inDuplicatedNumber(guessNumber):
            raise TypeError('중복된 숫자가 존재합니다')

    def inDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]