import re

class Token:
    def __init__(self, type, value):
        self.type = type 
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    __repr__ = __str__

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current_char = None
        self.pos = 0

        # Define the token types. This is a non-exhaustive list and should be
        # expanded according to the requirements of your specific language.
        self.token_types = [
            ('INTEGER', r'\d+'),
            ('FLOAT', r'\d+\.\d*'),
            ('PLUS', r'\+'),
            ('MINUS', r'\-'),
            ('MUL', r'\*'),
            ('DIV', r'\/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('EQ', r'\=='),
            ('NEQ', r'\!='),
            ('LT', r'\<'),
            ('GT', r'\>'),
            ('LE', r'\<='),
            ('GE', r'\>='),
            ('ASSIGN', r'\='),
            ('BEGIN', r'\{'),
            ('END', r'\}'),
            ('SEMI', r'\;'),
            ('VAR', r'\bvar\b'),
            ('IF', r'\bif\b'),
            ('PRINT', r'\bprint\b'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('WS', r'\s+')
        ]


    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        if self.pos == len(self.text):
            return None

        for token_type, token_regex in self.token_types:
            regex = re.compile(token_regex)
            match = regex.match(self.text, self.pos)
            if match:
                self.pos = match.end()
                if token_type != 'WS':  # Ignore whitespace
                    return Token(token_type, match.group())

        self.error()

    def tokenize(self):
        while token := self.get_next_token():
            self.tokens.append(token)

        return self.tokens

# Using the lexer
lexer = Lexer("var x = 3.14; if (x == 3.14) { print(x); }")
tokens = lexer.tokenize()
for token in tokens:
    print(token)
