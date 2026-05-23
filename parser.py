from lexer import Lexer
from formulas import *


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):

        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    def eat(self, token_type):

        token = self.current()

        if token and token.type == token_type:
            self.pos += 1
            return token

        raise SyntaxError(
            f"Esperado {token_type}"
        )

    def parse(self):
        return self.parse_iff()


    # BICONDICIONAL

    def parse_iff(self):

        left = self.parse_implication()

        while (
            self.current()
            and self.current().type == 'IFF'
        ):

            self.eat('IFF')

            right = self.parse_implication()

            left = Iff(left, right)

        return left


    # IMPLICAÇÃO

    def parse_implication(self):

        left = self.parse_or()

        token = self.current()

        if (
            token
            and token.type == 'IMPLIES'
        ):

            self.eat('IMPLIES')

            right = self.parse_implication()

            return Implies(left, right)

        return left


    # DISJUNÇÃO

    def parse_or(self):

        left = self.parse_xor()

        while (
            self.current()
            and self.current().type == 'OR'
        ):

            self.eat('OR')

            right = self.parse_xor()

            left = Or(left, right)

        return left


    # XOR

    def parse_xor(self):

        left = self.parse_and()

        while (
            self.current()
            and self.current().type == 'XOR'
        ):

            self.eat('XOR')

            right = self.parse_and()

            left = Xor(left, right)

        return left

def parse_formula(text):

    lexer = Lexer(text)

    tokens = lexer.tokenize()

    parser = Parser(tokens)

    return parser.parse()