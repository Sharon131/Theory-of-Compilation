#!/usr/bin/python
import AST
from SymbolTable import SymbolTable
from collections import defaultdict
from enum import Enum


class Type(Enum):
    AnyType = 0
    IntNumType = 1
    FloatNumType = 2
    StringType = 3
    RangeType = 4
    BoolType = 5
    ArrayType = 6


ttype = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: Type.AnyType
        ))
)

for op in '+-*/':
    ttype[op][Type.IntNumType][Type.IntNumType] = Type.IntNumType
    ttype[op][Type.IntNumType][Type.FloatNumType] = Type.FloatNumType
    ttype[op][Type.FloatNumType][Type.IntNumType] = Type.FloatNumType
    ttype[op][Type.FloatNumType][Type.FloatNumType] = Type.FloatNumType

for op in ['<', '<=', '>', '>=', '!=', '==']:
    ttype[op][Type.IntNumType][Type.IntNumType] = Type.BoolType
    ttype[op][Type.IntNumType][Type.FloatNumType] = Type.BoolType
    ttype[op][Type.FloatNumType][Type.IntNumType] = Type.BoolType
    ttype[op][Type.FloatNumType][Type.FloatNumType] = Type.BoolType

for op in ['==', '!=']:
    ttype[op][Type.StringType][Type.StringType] = Type.BoolType


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.table = SymbolTable()
        self.loop_counter = 0

    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_IntNum(self, node):
        return Type.IntNumType

    def visit_FloatNum(self, node):
        return Type.FloatNumType

    def visit_String(self, node):
        return Type.StringType

    def visit_Variable(self, node):
        type1 = self.table.get(node.name)
        if type1 is None:
            print("Line {0}: Variable {1} could not be found.".format(node.line_no, node.name))
        return type1

    def visit_Submatrix(self, node):
        # sprawdzić czy odwołania nie są poza macierz
        type1 = self.visit(node.var)  # get type of variable (add dimensions and list of sizes to type array)
        self.visit(node.vector)
        if type1 != Type.ArrayType:
            print("Line {0}: Cannot reference {1} like an array.".format(node.line_no, type1))
        return Type.ArrayType

    def visit_Vector(self, node):
        general_type = Type.AnyType
        size = len(node.values)
        elem_size = 1
        for value in node.values:
            type1 = self.visit(value)
            if node.values.index(value) == 0:
                if isinstance(type1, tuple):
                    general_type = Type.ArrayType
                    elem_size = type1[1]
                else:
                    general_type = type1

            if isinstance(type1, tuple):  # this means there's vector inside
                if type1[1] != elem_size:
                    print("Line {0}: Size of vectors in vector cannot be different.".format(value.line_no))
            else:
                if type1 not in [Type.IntNumType, Type.FloatNumType, Type.StringType]:
                    print("Line {0}: {1} could not be placed inside a vector.".format(value.line_no, type1))

                if ttype['+'][type1][general_type] == Type.AnyType:
                    print("Line {0}: {1} and {2} cannot be placed in the same vector.".format(value.line_no, type1, general_type))

        return general_type, size, elem_size

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)

        # checking if one of types isn't a matrix or vector
        if isinstance(type1, tuple) and isinstance(type2, tuple):
            # check length and general types
            elem_type1, size1, elem_size1 = type1
            elem_type2, size2, elem_size2 = type2

            if size1 != size2 or elem_size1 != elem_size2:
                print("Line {0}: Vectors' sizes are not the same.".format(node.line_no))
            if ttype[node.op][elem_type1][elem_type2] == Type.Any:
                print("Vectors have incompatible types for operation {node.operation}.")

        elif isinstance(type1, tuple):
            elem_type1, size1, elem_size1 = type1
            type1 = elem_type1
            if ttype[node.op][elem_type1][type2] == Type.AnyType:
                print("Line {0}: Cannot execute operation {1} for types {2} and {3}".format(node.line_no, node.op, elem_type1, type2))
        elif isinstance(type2, tuple):
            elem_type2, size2, elem_size2 = type2
            type2 = elem_type2
            if ttype[node.op][elem_type2][type1] == Type.AnyType:
                print("Line {0}: Cannot execute operation {1} for types {2} and {3}".format(node.line_no, node.op, elem_type2, type1))
        elif ttype[node.op][type1][type2] == Type.AnyType:
            print("Line {0}: Cannot execute operation {1} for {2} and {3}.".format(node.line_no, node.op, type1, type2))
        return ttype[node.op][type1][type2]

    def visit_UnaryExpr(self, node):
        type1 = self.visit(node.arg)
        if type1 != Type.IntNumType and type1 != Type.FloatNumType:
            print("Line {0}: Unary expression cannot be executed for {1}.".format(node.line_no, type1))
        return type1

    def visit_Assignment(self, node):
        type1 = self.visit(node.value)
        self.table.put(node.var.name, type1)

    def visit_BreakStatement(self, node):
        if self.loop_counter == 0:
            print("Line {0}: Break statement used outside of loop.".format(node.line_no))

    def visit_ContinueStatement(self, node):
        if self.loop_counter == 0:
            print("Line {0}: Continue statement used outside of loop.".format(node.line_no))

    def visit_ReturnStatement(self, node):
        if not self.table.isInFunction():
            print("Line {0}: Return used out of function.".format(node.line_no))
        self.visit(node.to_return)

    def visit_PrintStatement(self, node):
        self.visit(node.to_print) # check if not a list?
        return None

    def visit_RangeStatement(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        if type1 == type2 == Type.IntNumType:
            return Type.RangeType
        else:
            print("Line {0}: Range nums must be integers".format(node.line_no))
            return Type.RangeType

    def visit_IfStatement(self, node):
        type1 = self.visit(node.condition)

        if type1 != Type.BoolType:
            print("Line {0}: Evaluation of condition in if statement should be a boolean.".format(node.line_no))

        self.table.pushScope("if")
        self.visit(node.if_block)
        self.table.popScope()

        if node.else_block is not None:
            self.table.pushScope("else")
            self.visit(node.else_block)
            self.table.popScope()

    def visit_WhileLoop(self, node):
        type1 = self.visit(node.condition)

        if type1 != Type.BoolType:
            print("Line {0}: Evaluation of condition in while loop should be a boolean.".format(node.line_no))

        self.loop_counter += 1
        self.table.pushScope("while")
        self.visit(node.instructions)
        self.table.popScope()
        self.loop_counter -= 1

    def visit_ForLoop(self, node):
        # type1 = self.visit(node.var)
        type2 = self.visit(node.for_range)

        if type2 != Type.RangeType:
            print("Line {0}: Error in range".format(node.line_no))

        self.table.put(node.var, type2)

        self.loop_counter += 1
        self.table.pushScope("for")
        self.visit(node.instructions)
        self.table.popScope()
        self.loop_counter -= 1

    def visit_Error(self, node):
        print('Error in node ', node, " and line: ", node.line_no)
