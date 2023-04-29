import coverage
import unittest
from lexer import * 
from main import *


myProgram = 'def main ( int hehehaha ) { ( = varone 30 ) ( while varexpression break ) ( for varnamehere in expressionstring : break ) }'
myProgram = 'def optest ( string testing ) {  ( + 3 2 )  (  - THIS that )  (  / 3 2 )  (  // 3 2 )  (  % 3 2 )  }'
myProgram = '( pair int int )'
tokens = Tokenize(myProgram).tokenize()
print("result")


testingParse = Parser(tokens)
result = testingParse.parseType(0)
# result = testingParse.parseProgram(0)
print("this works")