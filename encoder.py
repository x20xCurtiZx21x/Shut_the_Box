'''
Author: Chase Curtis
email: curtischase6@gmail.com
Email any questions
'''

#encoder.py

class Encoder:

    def __init__(self, name = None, xp = None, level = None, money = None, prestige = None):

        self._name = name

        self._xp = xp

        self._level = level

        self._money = money

        self._prestige = prestige

    def encode(self):

        return f'{self.encode_xp(self._xp)}#{self.encode_level(self._level)}#{self._name}#{self.encode_money(self._money)}#{self.encode_prestige(self._prestige)}'

    def encode_xp(self, xp):

        return hex(xp)

    def encode_level(self, level):

        return hex(level)

    def encode_money(self, money):

        return hex(money)

    def encode_prestige(self, prestige):

        return hex(prestige)

    def decode(self, code):

        decode = code.split('#')

        self._name = decode[2]

        self._xp = int(decode[0], base = 16)

        self._level = int(decode[1], base = 16)

        self._money = int(decode[3], base = 16)

        self._prestige = int(decode[4], base = 16)