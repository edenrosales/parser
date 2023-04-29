#import coverage
import unittest
from main import *
from lexer import *

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser('')

    def test_parser_exp(self):
        self.parser.tokens = [('LeftParenToken', '('), ("PrintToken", "print"), ("INTEGER","2"),("RightParenToken",")")]
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(printExp(ParseResult(intExp('2'), 3)), 4)")

    def test_parser_type(self):
        myProgram = 'boolean'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseType(0)
        self.assertEqual(repr(result), "ParseResult(booleanType(None), 1)")

    def test_parser_type1(self):
        myProgram = 'string'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseType(0)
        self.assertEqual(repr(result), "ParseResult(stringType(None), 1)")

    def test_parser_type2(self):
        myProgram = '( pair int int )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseType(0)
        self.assertEqual(repr(result), "ParseResult(pairType(ParseResult(intType(None), 3), ParseResult(intType(None), 4)), 5)")

    def test_parser_type3(self):
        myProgram = '( pair boolean string )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseType(0)
        self.assertEqual(repr(result), "ParseResult(pairType(ParseResult(booleanType(None), 3), ParseResult(stringType(None), 4)), 5)")

    def test_parser_type4(self):
        myProgram = '( pair float T )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseType(0)
        self.assertEqual(repr(result), "ParseResult(pairType(ParseResult(floatType(None), 3), ParseResult(TType(None), 4)), 5)")

    def test_parser_stmt(self):
        myProgram = '( = varname 5 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseStmt(0)
        self.assertEqual(repr(result), "ParseResult(assignmentStmt('varname', ParseResult(intExp('5'), 4)), 5)")
    
    def test_parser_stmt1(self):
        myProgram = '( if 5 break  )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseStmt(0)
        self.assertEqual(repr(result), "ParseResult(ifElseStmt(ParseResult(intExp('5'), 3), ParseResult(breakStmt(None), 4), None), 5)")
    
    def test_parser_stmt2(self):
        myProgram = '( if 5 break else break )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseStmt(0)
        self.assertEqual(repr(result), "ParseResult(ifElseStmt(ParseResult(intExp('5'), 3), ParseResult(breakStmt(None), 4), ParseResult(breakStmt(None), 6)), 7)")

    def test_parser_stmt3(self):
        myProgram = '( return 5 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseStmt(0)
        self.assertEqual(repr(result), "ParseResult(returnStmt(ParseResult(intExp('5'), 3)), 3)")

    # def test_parser_stmt3(self):
    #     myProgram = '( return break )'
    #     self.parser.tokens = Tokenize(myProgram).tokenize()
    #     result = self.parser.parseStmt(0)
    #     self.assertEqual(repr(result), "ParseResult(assignmentStmt('varname', ParseResult(intExp('5'), 4)), 5)")

    def test_parser_exp3(self):
        myProgram = '(  % 3 2 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(opExp('%', ParseResult(intExp('3'), 3), ParseResult(intExp('2'), 4)), 5)")

    def test_parser_exp4(self):
        myProgram = '(  / 3 2 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(opExp('/', ParseResult(intExp('3'), 3), ParseResult(intExp('2'), 4)), 5)")

    def test_parser_exp5(self):
        myProgram = '(  - THIS that )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(opExp('-', ParseResult(varExp('THIS'), 3), ParseResult(varExp('that'), 4)), 5)")

    def test_parser_exp6(self):
        myProgram = '( fst 1 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(fstExp(ParseResult(intExp('1'), 3)), 4)")

    def test_parser_exp7(self):
        myProgram = '( snd 2 )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseExp(0)
        self.assertEqual(repr(result), "ParseResult(sndExp(ParseResult(intExp('2'), 3)), 4)")

    def test_parser_exp8(self):
        myProgram = '( var varname this )'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseVarDec(0)
        self.assertEqual(repr(result), "ParseResult(vardec('varname', ParseResult(varExp('this'), 4)), 5)")

    def test_parser_program(self):
        myProgram = 'def main ( int hehehaha ) { ( = varone 30 ) }'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseProgram(0)
        self.assertEqual(repr(result), "ParseResult(program(ParseResult(methodDef('main', ParseResult(intType(None), 4), 'hehehaha', [ParseResult(assignmentStmt('varone', ParseResult(intExp('30'), 11)), 12)]), 12)), 12)")

    def test_parser_program1(self):
        myProgram = 'def main ( int hehehaha ) { ( = varone 30 ) ( while varexpression break ) ( for varnamehere in expressionstring : break ) }'
        self.parser.tokens = Tokenize(myProgram).tokenize()
        result = self.parser.parseProgram(0)
        self.assertEqual(repr(result), "ParseResult(program(ParseResult(methodDef('main', ParseResult(intType(None), 4), 'hehehaha', [ParseResult(assignmentStmt('varone', ParseResult(intExp('30'), 11)), 12), ParseResult(whileStmt(ParseResult(varExp('varexpression'), 15), [ParseResult(breakStmt(None), 16)]), 17), ParseResult(forStmt('varnamehere', ParseResult(varExp('expressionstring'), 22), [ParseResult(breakStmt(None), 24)]), 25)]), 25)), 25)")

class TestTokenize(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenize('')

    def test_tokenize_number(self):
        self.tokenizer.code = '123 4.56'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('INTEGER', '123'), ('FLOAT', '4.56')])

    def test_tokenize_reserved_word_or_identifier(self):
        self.tokenizer.code = 'if foo bar'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('IfToken', 'if'), ('IDENTIFIER', 'foo'), ('IDENTIFIER', 'bar')])

    def test_tokenize_symbol(self):
        self.tokenizer.code = '== && ( ) = { } > < : + - * / % \"'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('DoubleEqualToken', '=='), ('LogicalAndToken', '&&'),
                                                 ('LeftParenToken', '('), ('RightParenToken', ')'),
                                                 ('SingleEqualToken', '='), ('LeftBraceToken', '{'),
                                                 ('RightBraceToken', '}'), ('GreaterThanToken', '>'),
                                                 ('LessThanToken', '<'), ('ColonToken', ':'), ('PlusToken', '+'),
                                                 ('MinusToken', '-'), ('MultiplicationToken', '*'),
                                                 ('DivisionToken', '/'), ('ModToken', '%'), ('DoubleQuoteToken', '\"')])

    def test_tokenize(self):
        self.tokenizer.code = '(while 5 < 2 (= a 3))'
        tokens = self.tokenizer.tokenize()
        self.assertEqual(tokens, [('LeftParenToken', '('), ('WhileToken', 'while'), ('INTEGER', '5'),
                                  ('LessThanToken', '<'), ('INTEGER', '2'), ('LeftParenToken', '('),
                                  ('SingleEqualToken', '='), ('IDENTIFIER', 'a'), ('INTEGER', '3'), ('RightParenToken', ')'), ('RightParenToken', ')')])

    def test_tokenize2(self):
        self.tokenizer.code = '(+ 3 2)'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('LeftParenToken', '('), ('PlusToken', '+'), ('INTEGER', '3'),
                                                 ('INTEGER', '2'), ('RightParenToken', ')')])

    def test_tokenize1(self):
        self.tokenizer.code = '(if (-5 3) == 6' \
                              '(print lastName))'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('LeftParenToken', '('), ('IfToken', 'if'), ('LeftParenToken', '('),
                                                 ('MinusToken', '-'), ('INTEGER', '5'), ('INTEGER', '3'), ('RightParenToken', ')'),
                                                 ('DoubleEqualToken', '=='), ('INTEGER', '6'),
                                                 ('LeftParenToken', '('), ('PrintToken', 'print'),
                                                 ('IDENTIFIER', 'lastName'), ('RightParenToken', ')'),
                                                 ('RightParenToken', ')')])


if __name__ == '__main__':
    # cov = coverage.Coverage()
    # cov.start()
    unittest.main()
    # cov.stop()
    # cov.save()
    # cov.report()