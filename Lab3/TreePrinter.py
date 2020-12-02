from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("|  " * indent + self.value)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.name))

    @addToClass(AST.Submatrix)
    def printTree(self, indent=0):
        print("|  " * indent + "SUBMATRIX")
        self.var.printTree(indent + 1)
        self.vector.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("|  " * indent + "VECTOR")
        for v in self.values:
            v.printTree(indent + 1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("|  " * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print("|  " * indent + self.op)
        self.arg.printTree(indent + 1)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("|  " * indent + self.op)
        # print("|  " * (indent + 1) + self.var)
        self.var.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.BreakStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "BREAK")

    @addToClass(AST.ContinueStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "CONTINUE")

    @addToClass(AST.ReturnStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.PrintStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "PRINT")
        for o in self.to_print:
            o.printTree(indent + 1)

    @addToClass(AST.RangeStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "RANGE")
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.IfStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "IF")
        self.condition.printTree(indent + 1)
        print("|  " * indent + "IF_BLOCK")
        self.if_block.printTree(indent + 1)
        if self.else_block is not None:
            print("|  " * indent + "ELSE_BLOCK")
            self.else_block.printTree(indent + 1)

    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):
        print("|  " * indent + "WHILE")
        self.condition.printTree(indent + 1)
        self.instructions.printTree(indent + 1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        print("|  " * indent + "FOR")
        self.var.printTree(indent + 1)
        self.for_range.printTree(indent + 1)
        self.instructions.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        print("| " * indent + "ERROR")

