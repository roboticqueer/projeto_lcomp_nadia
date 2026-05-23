import re


TOKEN_REGEX = [
    ('IFF', r'<->'),
    ('IMPLIES', r'->'),
    ('AND', r'&'),
    ('OR', r'\|'),
    ('XOR', r'\^'),
    ('NOT', r'~'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('ATOM', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('SPACE', r'\s+'),
]


class Token:

    def __init__(self, typ, value):
        self.type = typ
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"


class Lexer:

    def __init__(self, text):
        self.text = text

    def tokenize(self):

        tokens = []
        pos = 0

        while pos < len(self.text):

            match = None

            for token_type, pattern in TOKEN_REGEX:

                regex = re.compile(pattern)

                match = regex.match(
                    self.text,
                    pos
                )

                if match:

                    value = match.group(0)

                    if token_type != 'SPACE':
                        tokens.append(
                            Token(token_type, value)
                        )

                    pos = match.end(0)

                    break

            if not match:

                raise SyntaxError(
                    f"Símbolo inválido: "
                    f"{self.text[pos:]}"
                )

        return tokens