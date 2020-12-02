
class Node(object):
    pass


class Instructions(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class Submatrix(Node):
    def __init__(self, var, vector):
        self.var = var
        self.vector = vector


class Vector(Node):
    def __init__(self, values):
        self.values = values


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg


class Assignment(Node):
    def __init__(self, var, op, value):
        self.var = var
        self.op = op
        self.value = value


class BreakStatement(Node):
    def __init__(self):
        pass


class ContinueStatement(Node):
    def __init__(self):
        pass


class ReturnStatement(Node):
    def __init__(self, to_return):
        self.to_return = to_return


class PrintStatement(Node):
    def __init__(self, to_print):
        self.to_print = to_print


class RangeStatement(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class IfStatement(Node):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block


class WhileLoop(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class ForLoop(Node):
    def __init__(self, var, for_range, instructions):
        self.var = var
        self.for_range = for_range
        self.instructions = instructions


class Error(Node):
    def __init__(self):
        pass


from TreePrinter import addToClass
