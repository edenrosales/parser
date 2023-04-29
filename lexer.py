class Tokenize:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.tokens = []

    class TokenizeException(Exception):
        pass

    def tokenize_number(self):
        digits = ''
        is_float = False
        while (self.position < len(self.code) and self.code[self.position].isdigit()) or (self.position < len(self.code) and self.code[self.position] == "."):
            if self.code[self.position] == ".":
                is_float = True
            digits += self.code[self.position]
            self.position += 1
        if len(digits) > 0:
            if is_float:
                self.tokens.append(('FLOAT', digits))
            else:
                self.tokens.append(('INTEGER', digits))

    def tokenize_reserved_word_or_identifier(self):
        name = ''
        if self.position < len(self.code) and self.code[self.position].isalpha():
            name += self.code[self.position]
            self.position += 1
            while self.position < len(self.code) and self.code[self.position].isalnum():
                name += self.code[self.position]
                self.position += 1

        if len(name) > 0:
            if name == 'if':
                self.tokens.append(('IfToken', name))
            elif name == 'while':
                self.tokens.append(('WhileToken', name))
            elif name == 'for':
                self.tokens.append(('ForToken', name))
            elif name == 'var':
                self.tokens.append(('VarToken', name))
            elif name == 'def':
                self.tokens.append(('DefToken', name))
            elif name == 'print':
                self.tokens.append(('PrintToken', name))
            elif name == 'pair': 
                self.tokens.append(('PairToken', name))
            # elif name == 'op': 
            #     self.tokens.append(('OpToken', name))
            elif name == 'fst': 
                self.tokens.append(('FSTToken', name))
            elif name == 'snd': 
                self.tokens.append(('SNDToken', name))
            elif name == 'return': 
                self.tokens.append(('ReturnToken', name))
            elif name == 'break': 
                self.tokens.append(('BreakToken', name))
            elif name == 'true': 
                self.tokens.append(("TrueToken", name))
            elif name == 'false': 
                self.tokens.append(("FalseToken", name))
            elif name == "int":
                self.tokens.append(("IntTypeToken", name))
            elif name == "boolean":
                self.tokens.append(("BooleanTypeToken", name))
            elif name == "string":
                self.tokens.append(("StringTypeToken", name))
            elif name == "float":
                self.tokens.append(("FloatTypeToken", name))
            elif name == "T":
                self.tokens.append(("TTypeToken", name))
            elif name == "in":
                self.tokens.append(("InToken",name))
            elif name == "else":
                self.tokens.append(("ElseToken", name))
            else:
                self.tokens.append(('IDENTIFIER', name))#this will handle identifiers and also strings so just be careful
            

    def tokenize_symbol(self):
        if self.position + 1 < len(self.code):
            if self.code[self.position:self.position + 2] == '==':
                self.tokens.append(('DoubleEqualToken', '=='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '>=':
                self.tokens.append(('GreaterOrEqualToken', '>='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '<=':
                self.tokens.append(('LessOrEqualToken', '<='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '&&':
                self.tokens.append(('LogicalAndToken', '&&'))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '||':
                self.tokens.append(('LogicalOrToken', '||'))
                self.position += 2
        if self.code[self.position] == '(':
            self.tokens.append(('LeftParenToken', '('))
            self.position += 1
        elif self.code[self.position] == ')':
            self.tokens.append(('RightParenToken', ')'))
            self.position += 1
        elif self.code[self.position] == '=':
            self.tokens.append(('SingleEqualToken', '='))
            self.position += 1
        elif self.code[self.position] == '{':
            self.tokens.append(('LeftBraceToken', '{'))
            self.position += 1
        elif self.code[self.position] == '}':
            self.tokens.append(('RightBraceToken', '}'))
            self.position += 1
        elif self.code[self.position] == '<':
            self.tokens.append(('LessThanToken', '<'))
            self.position += 1
        elif self.code[self.position] == '>':
            self.tokens.append(('GreaterThanToken', '>'))
            self.position += 1
        elif self.code[self.position] == ':':
            self.tokens.append(('ColonToken', ':'))
            self.position += 1
        elif self.code[self.position] == '+':
            self.tokens.append(('PlusToken', '+'))
            self.position += 1
        elif self.code[self.position] == '-':
            self.tokens.append(('MinusToken', '-'))
            self.position += 1
        elif self.code[self.position] == '*':
            self.tokens.append(('MultiplicationToken', '*'))
            self.position += 1
        elif self.code[self.position] == '/':
            self.tokens.append(('DivisionToken', '/'))
            self.position += 1
        elif self.code[self.position] == '//':
            self.tokens.append(('DoubleDivisionToken', '/'))
            self.position += 1
        elif self.code[self.position] == '%':
            self.tokens.append(('ModToken', '%'))
            self.position += 1
        elif self.code[self.position] == '\"':
            self.tokens.append(('DoubleQuoteToken', '\"'))
            self.position += 1
    # def tokenizeStatement(self):

    def tokenize(self):
        while self.position < len(self.code):
            cur_pos = self.position
            if self.code[self.position] == ' ':
                self.position += 1
            elif self.code[self.position].isdigit():
                self.tokenize_number()
            elif self.code[self.position].isalpha():
                self.tokenize_reserved_word_or_identifier()
            else:
                self.tokenize_symbol()
            if cur_pos == self.position:
                raise self.TokenizeException(f'Couldn\'t parse this character {self.code[self.position]}')
        return self.tokens

myProgram = 'def main ( int hehehaha ) { ( = varone 30 ) }'
tokens = Tokenize(myProgram).tokenize()
print("result")