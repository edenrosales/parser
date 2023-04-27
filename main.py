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
    
class boolType(type):
    def __init__(self):
        return None
    def toString():
        return "boolType"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "boolType"
    
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

class T(type):
    def __init__(self):
        return None
    def toString():
        return "T"
    def hashCode():
        return 0
    def equals(thing):
        return thing.toString() == "T"

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
    def __init__(self,leftValue , rightValue):
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
