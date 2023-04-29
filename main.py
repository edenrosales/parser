class type:
    def __init__(self):
        return None
    
class intType(type):
    def __init__(self):
        return None
    def toString():
        return "intType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "intType"
    
class booleanType(type):
    def __init__(self):
        return None
    def toString():
        return "booleanType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "booleanType"
    
class stringType(type):
    def __init__(self):
        return None
    def toString():
        return "stringType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "stringType"

class floatType(type):
    def __init__(self):
        return None
    def toString():
        return "floatType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "floatType"

class TType(type):
    def __init__(self):
        return None
    def toString():
        return "TType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "TType"

class pairType(type):
    def __init__(self,leftType,rightType):
        self.leftType = leftType
        self.rightType = rightType  
    def toString():
        return "pairType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "pairType"
class op:
    def __init__(self):
        return None

class plusOp(op):
    def __init__(self):
        return None
    def toString():
        return "plusOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "plusOp"

class minusOp(op):
    def __init__(self):
        return None
    def toString():
        return "minusOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "minusOp"
    
class starOp(op):
    def __init__(self):
        return None
    def toString():
        return "starOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "starOp"
    
class oneDashOp(op):
    def __init__(self):
        return None
    def toString():
        return "oneDashOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "oneDashOp"

class twoDashOp(op):
    def __init__(self):
        return None
    def toString():
        return "twoDashOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "twoDashOp"
    
class modOp(op):
    def __init__(self):
        return None
    def toString():
        return "modOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "modOp"
    

class exp:
    def __init__(self):
        return None

class varExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "varExp"
    def toString():
        return "varExp"

class strExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "strExp"
    def toString():
        return "strExp"

class intExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "intExp"
    def toString():
        return "intExp"
    
class floatExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "floatExp"
    def toString():
        return "floatExp"

class printExp(exp):
    def __init__(self,value):
        self.exp = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "printExp"
    def toString():
        return "printExp"

class opExp(exp):
    def __init__(self,operation, leftValue , rightValue):
        self.operation = operation
        self.leftExp = leftValue
        self.rightExp = rightValue
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "opExp"
    def toString():
        return "opExp"

class methodnameExp(exp):
    def __init__(self,expressions):
        self.exps = expressions
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "methodnameExp"
    def toString():
        return "methodnameExp"

class pairExp(exp):
    def __init__(self,leftExpression,rightExpression):
        self.leftExp = leftExpression
        self.rightExp = rightExpression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "pairExp"
    def toString():
        return "pairExp"

class fstExp(exp):
    def __init__(self,expression):
        self.exp = expression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "fstExp"
    def toString():
        return "fstExp"

class sndExp(exp):
    def __init__(self,expression):
        self.exp = expression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "sndExp"
    def toString():
        return "sndExp"

class vardec:
    def __init__(self,varname, expression):
        self.varname = varname
        self.expression = expression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "vardec"
    def toString():
        return "vardec"

#i am going to treat vardec as a statement here - because it ultimately is
class stmt:
    def __init__(self):
        return None
    
class vardecStmt(stmt):
    def __init__(self, varname, exp):
        self.varname = varname
        self.exp = exp
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "vardecStmt"
    def toString():
        return "vardecStmt"

class assignmentStmt(stmt):
    def __init__(self, varname, exp):
        self.varname = varname
        self.exp = exp
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "assignmentStmt"
    def toString():
        return "assignmentStmt"
    
class whileStmt(stmt):
    def __init__(self, exp, stmt):
        self.exp = exp
        self.stmt = stmt
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "whileStmt"
    def toString():
        return "whileStmt"
    
class forStmt(stmt):
    def __init__(self, var, exp, stmt):
        self.var = var 
        self.exp = exp
        self.stmt = stmt
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "forStmt"
    def toString():
        return "forStmt"
    
class breakStmt(stmt):
    def __init__(self):
        return None
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "breakStmt"
    def toString():
        return "breakStmt"

class ifElseStmt(stmt):
    def __init__(self, exp,stmt,optionalStmt):
        self.exp = exp 
        self.then = stmt 
        self.optionalElse = optionalStmt
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "ifElseStmt"
    def toString():
        return "ifElseStmt"

class returnStmt(stmt):
    def __init__(self, exp):
        self.optionalExp = exp
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "returnStmt"
    def toString():
        return "returnStmt"

class methodDef:
    def __init__(self,methodName,methodType,varName,stmt):
        self.methodName = methodName
        self.type = methodType
        self.varName = varName
        self.stmt = stmt 
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "methodDef"
    def toString():
        return "methodDef"

class program: 
    def __init__(self,method):
        self.methods = method
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "program"
    def toString():
        return "program"


class ParseResult: 
    def __init__(self,result, nextPosition):
        self.result= result
        self.nextPos = nextPosition
    
class Parser: 
    def __init__(self,tokens):
        self.tokens = tokens 
        self.position = 0
    def parseExp(self, position):
        if self.tokens[position][0] == "VarToken":
            return ParseResult(varExp(self.tokens[position][1]),position + 1)
        elif self.tokens[position][0] == "DoubleQuoteToken": 
            position += 1
            if self.tokens[position+1][0] == "DoubleQuoteToken":
                return ParseResult(strExp(self.tokens[position][1]),position + 2 )
            else:
                raise Exception("Parser: String Failure")
        elif self.tokens[position][0] == "INTEGER":
            return ParseResult(intExp(self.tokens[position][1]), position+ 1)
        elif self.tokens[position][0] == "FLOAT":
            return ParseResult(floatExp(self.tokens[position][1]), position + 1)
        elif self.tokens[position][0] == "IDENTIFIER":
            return ParseResult(varExp(self.tokens[position][1]), position + 1)
        elif self.tokens[position][0] == "LeftParenToken":
            position += 1
            if self.tokens[position][0] == "PrintToken":
                expression = self.parseExp(position+1)
                position = expression.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(printExp(expression),position + 1 )   
            elif self.tokens[position][0] in ("PlusToken", "MinusToken","MultiplicationToken","DivisionToken","DoubleDivisionToken","ModToken"):
                operation = self.tokens[position][1]
                position += 1 
                leftExpression = self.parseExp(position)
                rightExpression = self.parseExp(leftExpression.nextPos)
                position = rightExpression.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(opExp(operation,leftExpression,rightExpression),position + 1)
            elif self.tokens[position][0] == "IDENTIFIER":
                expressions = self.parseExp(position+1)
                position = expressions.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(methodnameExp(expressions),position+1)
            elif self.tokens[position][0] == "PairToken":
                leftExpression = self.parseExp(position+ 1)
                rightExpression = self.parseExp(leftExpression.nextPos)
                position = rightExpression.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(pairExp(leftExpression,rightExpression),position + 1)
            elif self.tokens[position][0] == "FSTToken":
                expression = self.parseExp(position+1)
                position = expression.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(fstExp(expression),position + 1 )   
            elif self.tokens[position][0] == "SNDToken":
                expression = self.parseExp(position+1)
                position = expression.nextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(sndExp(expression),position + 1 )   
            else: 
                raise Exception("Parser Error")
        
    # WE HAVE TO BE CAREFUL FOR THE PAIR TOKEN BECAUSE IT CAN BOTH BE A DECLARATION IF THERE ARE EXPRESSOINS INSIDE OR A TYPE IF THERE ARE TYPES INSIDE
    def parseType(self,position): 
        if self.tokens[position][0] == "IntTypeToken": 
            return ParseResult(intType(),position + 1)
        elif self.tokens[position][0] == "BooleanTypeToken":
            return ParseResult(booleanType(),position+1)
        elif self.tokens[position][0] == "StringTypeToken":
            return ParseResult(stringType(),position+1)
        elif self.tokens[position][0] == "FloatTypeToken":
            return ParseResult(floatType(),position+1)
        elif self.tokens[position][0] == "TTypeToken":
            return ParseResult(TType(),position+1)
        elif self.tokens[position][0] == "LeftParenToken":
            leftType = self.parseType(position+ 1)
            rightType = self.parseType(leftType.nextPos)
            position = rightType.nextPos
            if self.tokens[position][0] == "RightParenToken":
                return ParseResult(pairType(leftType,rightType), position+ 1)
            else:
                raise Exception("Type Syntax Error")
        else:
            raise Exception("Type Syntax Error")
    
    def parseOp(): #we handle this inline when we need to - didnt abstract this out
        return None
    def parseVarDec(self,position):
        if self.tokens[position][0] == "LeftParenToken" and self.tokens[position+1][0] == "VarToken" and self.tokens[position+2][0] == "IDENTIFIER":
            varname = self.tokens[position+2][1]
            position+= 3
            expression = self.parseExp(position)
            if self.tokens[expression.nextPos][0] == "RightParenToken":
                return ParseResult(vardec(varname,expression), expression.nextPos + 1)
            else:
                raise Exception("Vardec syntax error")
        else:
            raise Exception("Vardec Syntax Error")
    
    def parseStmt(self,position):
        if self.tokens[position][0] == "BreakToken":
            return ParseResult(breakStmt(),position + 1)
        elif self.tokens[position][0] == "LeftParenToken":
            position += 1
            if self.tokens[position][0] == "SingleEqualToken" and self.tokens[position+1][0] == "IDENTIFIER":
                varname = self.tokens[position+1][1]
                position += 2
                expression = self.parseExp(position)
                if self.tokens[expression.nextPos][0] == "RightParenToken":
                    return ParseResult(assignmentStmt(varname,expression), expression.nextPos + 1)
                else:
                    raise Exception("Statemewnt Syntax Error")
            elif self.tokens[position][0] == "WhileToken":
                expression = self.parseExp(position + 1)
                position = expression.nextPos
                statements = [] 
                while self.tokens[position][0] == "LeftParenToken" or self.tokens[position][0] == "BreakToken":
                    statement = self.parseStmt(position)
                    position = statement.nextPos
                    statements.append(statement)
                position = statement.nextPos if len(statements) > 0 else position
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(whileStmt(expression,statements), position + 1)
                else:
                    raise Exception("Statemewnt Syntax Error")
            elif self.tokens[position][0] == "ForToken" and self.tokens[position+1][0] == "IDENTIFIER" and self.tokens[position+ 2][0] == "InToken":
                varname = self.tokens[position + 1][1]
                position += 3
                expression = self.parseExp(position)
                position = expression.nextPos
                if self.tokens[position][0] == "ColonToken":
                    position += 1 
                    
                    statements = self.parseStmt(position)
                    position = statements.nextPos
                    if self.tokens[position][0] == "RightParenToken":
                        return ParseResult(forStmt(varname,expression,statements), position + 1)
                    else:
                        raise Exception("Statemewnt Syntax Error")
                raise Exception("Statemewnt Syntax Error")
            elif self.tokens[position][0] == "IfToken" and self.tokens[position+1][0] == "IfToken":
                position += 2
                expression = self.parseExp(position)
                position = expression.nextPos
                statementTrue = self.parseStmt(position)
                position = statementTrue.neextPos
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(ifElseStmt(expression,statementTrue,None),position + 1)
                else:
                    statementFalse = self.parseStmt(position + 1)
                    position = statementFalse.nextPos
                    if self.tokens[position][0] == "RightParenToken":
                        return ParseResult(ifElseStmt(expression,statementTrue,statementFalse), position  +1)
                    else: 
                        raise Exception("Statemewnt Syntax Error")
            elif self.tokens[position][0] == "ReturnToken":
                position += 1
                if self.tokens[position][0] == "RightParenToken":
                    return ParseResult(returnStmt(None),position+1)
                else:
                    expression = self.parseExp(position)
                    if self.tokens[expression.nextPos][0] == "RightParenToken":
                        return ParseResult(returnStmt(expression),expression.nextPos)
                    else:
                        raise Exception("Statemewnt Syntax Error")
            else:
                raise Exception("Statemewnt Syntax Error")
        else:
            raise Exception("Statement Syntax Error")
    def parseMethodDef(self,position):
        if self.tokens[position][0] == "DefToken" and self.tokens[position+1][0] == "IDENTIFIER" and self.tokens[position+2][0] == "LeftParenToken":
            methodname = self.tokens[position+1][1]
            position += 3
            typeName = self.parseType(position)
            position = typeName.nextPos
            if self.tokens[position][0] == "IDENTIFIER" and self.tokens[position+1][0]=="RightParenToken" and self.tokens[position+2][0] == "LeftBraceToken":
                varname = self.tokens[position][1]
                position += 3
                statements = []
                while self.tokens[position][0] == "LeftParenToken" or self.tokens[position][0] == "BreakToken":
                    nextStatement = self.parseStmt(position)
                    position = nextStatement.nextPos
                    statements.append(nextStatement)            
                position = statements[-1].nextPos if len(statements) > 0 else position
                if self.tokens[position][0] == "RightBraceToken":
                    return ParseResult(methodDef(methodname,typeName,varname,statements),position)
                else:
                    raise Exception("Statemewnt Syntax Error")
            else: 
                raise Exception("Statemewnt Syntax Error")
        else: 
            raise Exception("Statemewnt Syntax Error")

    def parseProgram(self,position):
        methodDef = self.parseMethodDef(position)
        return ParseResult(program(methodDef),methodDef.nextPos)

    
tokens = [('LeftParenToken', '('), ('PlusToken', '+'), ('LeftParenToken', '('),('PlusToken', '+'),('INTEGER', '2'), ('INTEGER', '3'), ('RightParenToken', ')'), ('LeftParenToken', '('), ('PlusToken', '+'),('INTEGER', '3'), ('INTEGER', '2'), ('RightParenToken', ')'),('RightParenToken', ')')]
testingParse = Parser(tokens)
result = testingParse.parseExp(0)


tokens = [('LeftParenToken', '('),('PlusToken', '+'),('INTEGER', '2'), ('INTEGER', '3'), ('RightParenToken', ')')]
testingParse = Parser(tokens)
result = testingParse.parseExp(0)

tokens = [('LeftParenToken', '('), ("PrintToken", "print"), ("INTEGER","2"),("RightParenToken",")")] 
testingParse = Parser(tokens)
result = testingParse.parseExp(0)
print("this works")