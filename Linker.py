# Assuming ide.py provides an interface class called IDEInterface
from Ide import IDEInterface
from lexer import lexer, parser

class Linker:
    def __init__(self):
        self.interface = IDEInterface()

    def run(self):
        while True:
            source_code = self.interface.get_input()
            if source_code is None:
                break

            try:
                lexer = lexer(source_code)
                tokens = lexer.tokenize()
                parser = parser(tokens)
                result = parser.parse()
                self.interface.display_output(result)
            except Exception as e:
                self.interface.display_error(str(e))

if __name__ == '__main__':
    linker = Linker()
    linker.run()