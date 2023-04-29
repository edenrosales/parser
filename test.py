import coverage
import unittest
from lexer import * 
from main import *


myProgram = 'def main ( int hehehaha ) { ( = varone 30 ) }'
tokens = Tokenize(myProgram).tokenize()
print("result")

testingParse = Parser(tokens)
result = testingParse.parseProgram(0)
print("this works")