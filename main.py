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
    def __repr__(self):
        return f"intType({repr(None)})"   
    
class booleanType(type):
    def __init__(self):
        return None
    def toString():
        return "booleanType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "booleanType"
    def __repr__(self):
        return f"booleanType({repr(None)})"   
    
class stringType(type):
    def __init__(self):
        return None
    def toString():
        return "stringType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "stringType"
    def __repr__(self):
        return f"stringType({repr(None)})"   

class floatType(type):
    def __init__(self):
        return None
    def toString():
        return "floatType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "floatType"
    def __repr__(self):
        return f"floatType({repr(None)})"   

class TType(type):
    def __init__(self):
        return None
    def toString():
        return "TType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "TType"
    def __repr__(self):
        return f"TType({repr(None)})"   

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
    def __repr__(self):
        return f"pairType({repr(self.leftType)}, {repr(self.rightType)})"
    
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
    def __repr__(self):
        return f"plusOp({repr(None)})"   

class minusOp(op):
    def __init__(self):
        return None
    def toString():
        return "minusOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "minusOp"
    def __repr__(self):
        return f"minusOp({repr(None)})"    
    
class starOp(op):
    def __init__(self):
        return None
    def toString():
        return "starOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "starOp"
    def __repr__(self):
        return f"starOp({repr(None)})"    
    
class oneDashOp(op):
    def __init__(self):
        return None
    def toString():
        return "oneDashOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "oneDashOp"
    def __repr__(self):
        return f"oneDashOp({repr(None)})"    

class twoDashOp(op):
    def __init__(self):
        return None
    def toString():
        return "twoDashOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "twoDashOp"
    def __repr__(self):
        return f"twoDashOp({repr(None)})"    
    
class modOp(op):
    def __init__(self):
        return None
    def toString():
        return "modOp"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "modOp"
    def __repr__(self):
        return f"modOp({repr(None)})"    

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
    def __repr__(self):
        return f"varExp({repr(self.value)})"

class strExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "strExp"
    def toString():
        return "strExp"
    def __repr__(self):
        return f"strExp({repr(self.value)})"

class intExp(exp):
    def __init__(self,value):
        self.value = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "intExp"
    def toString():
        return "intExp"
    def __repr__(self):
        return f"intExp({repr(self.value)})"

class floatExp(exp):	
    def __init__(self,value):	
        self.value = value	
    def hashCode():	
        return 0	
    def equals(thing):	
        return thing.toString() == "floatExp"	
    def toString():	
        return "floatExp"
    def __repr__(self):
        return f"floatExp({repr(self.value)})"

class printExp(exp):
    def __init__(self,value):
        self.exp = value
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "printExp"
    def toString():
        return "printExp"
    def __repr__(self):
        return f"printExp({repr(self.exp)})"
    

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
    def __repr__(self):
        return f"opExp({repr(self.operation)}, {repr(self.leftExp)}, {repr(self.rightExp)})"

class methodnameExp(exp):
    def __init__(self,expressions):
        self.exps = expressions
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "methodnameExp"
    def toString():
        return "methodnameExp"
    def __repr__(self):
        return f"methodnameExp({repr(self.exps)})"

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
    def __repr__(self):
        return f"pairExp({repr(self.leftExp)}, {repr(self.rightExp)})"

class fstExp(exp):
    def __init__(self,expression):
        self.exp = expression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "fstExp"
    def toString():
        return "fstExp"
    def __repr__(self):
        return f"fstExp({repr(self.exp)})"

class sndExp(exp):
    def __init__(self,expression):
        self.exp = expression
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "sndExp"
    def toString():
        return "sndExp"
    def __repr__(self):
        return f"sndExp({repr(self.exp)})"
    
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
    def __repr__(self):
        return f"vardec({repr(self.varname)}, {repr(self.expression)})"

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
    def __repr__(self):
        return f"vardecStmt({repr(self.varname)}, {repr(self.exp)})"   

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
    def __repr__(self):
        return f"assignmentStmt({repr(self.varname)}, {repr(self.exp)})"   
    
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
    def __repr__(self):
        return f"whileStmt({repr(self.exp)}, {repr(self.stmt)})"   
    
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
    def __repr__(self):
        return f"forStmt({repr(self.var)}, {repr(self.exp)}, {repr(self.stmt)})"   
    
class breakStmt(stmt):
    def __init__(self):
        return None
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "breakStmt"
    def toString():
        return "breakStmt"
    def __repr__(self):
        return f"breakStmt({repr(None)})"  

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
    def __repr__(self):
        return f"ifElseStmt({repr(self.exp)}, {repr(self.then)}, {repr(self.optionalElse)})"  

class returnStmt(stmt):
    def __init__(self, exp):
        self.optionalExp = exp
    def hashCode():
        return 0 
    def equals(thing):
        return thing.toString() == "returnStmt"
    def toString():
        return "returnStmt"
    def __repr__(self):
        return f"returnStmt({repr(self.optionalExp)})"  

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
    def __repr__(self):
        return f"methodDef({repr(self.methodName)}, {repr(self.type)}, {repr(self.varName)}, {repr(self.stmt)})"

class program: 
    def __init__(self,method):
        self.methods = method
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "program"
    def toString():
        return "program"
    def __repr__(self):
        return f"program({repr(self.methods)})"

class ParseResult: 
    def __init__(self,result, nextPosition):
        self.result= result
        self.nextPos = nextPosition

    def __repr__(self):
        return f"ParseResult({(self.result)}, {self.nextPos})"
    
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
                    statements = []
                    while self.tokens[position][0] == "LeftParenToken" or self.tokens[position][0] == "BreakToken":
                        statement = self.parseStmt(position)
                        position = statement.nextPos
                        statements.append(statement)
                    position = statement.nextPos if len(statements) > 0 else position
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