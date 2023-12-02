import re
import pdb # this is to
import ast

TOKEN_TYPES = {
    'NUMBER': r'\d+(\.\d*)?',
    'IDENTIFIER': r'[a-zA-Z_]\w*',
    'OPERATOR': r'[+\-*/]',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'COMMA': r',',
    'WHITESPACE': r'\s+',
    'UNKNOWN': r'.'
}

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_index = 0

    def tokenize(self):
        while self.current_index < len(self.source_code):
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.current_index)
                if match:
                    if token_type != 'WHITESPACE':  # Skip whitespace
                        value = match.group(0)
                        self.tokens.append(Token(token_type, value))
                    self.current_index = match.end()
                    break
            else:
                raise ValueError(f"Unknown token at index {self.current_index}")
        return self.tokens

# Usage Example
if __name__ == '__main__':
    source_code = "3 + (2 * avg(4, 8))"
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)

       