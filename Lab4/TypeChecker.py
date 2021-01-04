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
        type1 = self.visit(node.var)  # get type of variable
        self.visit(node.vector)
        if not isinstance(type1, tuple):
            print("Line {0}: Cannot reference {1} like an array, var {2}.".format(node.var.line_no, type1, node.var.name))
        else:
            if type1[1] < len(node.vector.values):
                print("Line {0}: Matrix {1} has less dimensions than reference.".format(node.var.line_no, node.var.name))
            for indx in range(type1[1]):
                # type2 = self.visit(node.vector.values[indx])
                # if type2 != Type.IntNumType:
                #     print("Line {0}: Matrix reference must be an integer.".format(node.line_no))
                # else:
                ref = node.vector.values[indx].value
                if ref > type1[2][indx]-1:
                    print("Line {0}: Vector size in dimension {1} is {2} not {3}".format(node.var.line_no, indx, type1[2][indx], ref))
        return type1

    # Creating vector. Vector type description: (general_type, dimensions_no, list_of_sizes, elems_no)
    def visit_Vector(self, node):
        general_type = Type.AnyType
        dims_no = 1
        size = len(node.values)
        elem_size = 1
        list_of_sizes = []
        for value in node.values:
            type1 = self.visit(value)
            if node.values.index(value) == 0:
                if isinstance(type1, tuple):
                    general_type = type1[0]
                    elem_size = type1[3]
                    dims_no = type1[1] + 1
                    list_of_sizes = type1[2] + [size]
                else:
                    general_type = type1

            if isinstance(type1, tuple):  # this means there's vector inside
                if type1[3] != elem_size:
                    print("Line {0}: Sizes of subvectors cannot be different.".format(value.line_no))
                if type1[1] != dims_no - 1:
                    print("Line {0}: Subvectors must have the same number of dimensions.".format(value.line_no))
                if ttype['+'][general_type][type1[0]] == Type.AnyType:
                    print("Line {0}: {1} and {2} cannot be placed in the same vector.".format(value.line_no, type1[0], general_type))
            else:
                if type1 not in [Type.IntNumType, Type.FloatNumType, Type.StringType]:
                    print("Line {0}: {1} could not be placed inside a vector.".format(value.line_no, type1))

                if ttype['+'][type1][general_type] == Type.AnyType:
                    print("Line {0}: {1} and {2} cannot be placed in the same vector.".format(value.line_no, type1, general_type))

        if dims_no == 1:
            list_of_sizes = [size]
        return general_type, dims_no, list_of_sizes, elem_size*size

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)

        # checking if one of types isn't a matrix or vector
        if isinstance(type1, tuple) and isinstance(type2, tuple):
            # check length and general types
            elem_type1, dims_no1, list_of_sizes1, elems_no1 = type1
            elem_type2, dims_no2, list_of_sizes2, elems_no2 = type2

            if dims_no1 != dims_no2:
                print("Line {0}: Vectors must have the same number of dimensions.".format(node.left.line_no))
            if elems_no1 != elems_no2:
                print("Line {0}: Vectors for operation {1} should have the same sizes.".format(node.left.line_no, node.op))
            if ttype[node.op][elem_type1][elem_type2] == Type.AnyType:
                print("Line {0}: Vectors have incompatible types for operation {1}.".format(node.left.line_no, node.op))
            type1 = elem_type1
            type2 = elem_type2

        elif isinstance(type1, tuple):
            elem_type1, dims_no1, list_of_sizes1, elems_no1 = type1
            type1 = elem_type1
            if node.op not in ['.+', '.-', '.*', './'] or ttype[node.op[1]][elem_type1][type2] == Type.AnyType:
                print("Line {0}: Cannot execute operation {1} for ArrayType of {2}s and {3}".format(node.left.line_no, node.op, elem_type1, type2))
        elif isinstance(type2, tuple):
            elem_type2, dims_no2, list_of_sizes2, elems_no2 = type2
            type2 = elem_type2
            if node.op not in ['.+', '.-', '.*', './'] or ttype[node.op[1]][elem_type2][type1] == Type.AnyType:
                print("Line {0}: Cannot execute operation {1} for ArrayType of {2}s and {3}".format(node.left.line_no, node.op, elem_type2, type1))
        elif ttype[node.op][type1][type2] == Type.AnyType:
            print("Line {0}: Cannot execute operation {1} for {2} and {3}.".format(node.left.line_no, node.op, type1, type))
        return ttype[node.op][type1][type2]

    def visit_UnaryExpr(self, node):
        type1 = self.visit(node.arg)
        if type1 != Type.IntNumType and type1 != Type.FloatNumType:
            print("Line {0}: Unary expression {1} cannot be executed for {2}.".format(node.line_no, node.op, type1))
        return type1

    def visit_CreateMatrix(self, node):
        dims_no = len(node.arg)
        sizes = []
        elems_no = 1
        for elem in node.arg:
            type1 = self.visit(elem)
            if type1 != Type.IntNumType:
                print("Line {0}: {1} can use only integers as arguments".format(node.line_no, node.op))
            sizes.append(elem.value)
            elems_no *= elem.value

        return Type.IntNumType, dims_no, sizes, elems_no

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
        # self.visit(node.to_print)  # check if not a list?
        for elem in node.to_print:
            self.visit(elem)
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
