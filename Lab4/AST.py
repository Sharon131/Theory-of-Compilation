# add detecting functions
# detecting wrong matrix recall
# add checking eye,zeros,ones
class Node(object):
    # def __init__(self, lineno):
    #     self.lineno = lineno
    pass


class Instructions(Node):
    def __init__(self, instructions, line_no):
        self.line_no = line_no
        self.instructions = instructions


class IntNum(Node):
    def __init__(self, value, line_no):
        self.line_no = line_no
        self.value = value


class FloatNum(Node):
    def __init__(self, value, line_no):
        self.line_no = line_no
        self.value = value


class String(Node):
    def __init__(self, value, line_no):
        self.line_no = line_no
        self.value = value


class Variable(Node):
    def __init__(self, name, line_no):
        self.line_no = line_no
        self.name = name


class Submatrix(Node):
    def __init__(self, var, vector, line_no):
        self.line_no = line_no
        self.var = var
        self.vector = vector


class Vector(Node):
    def __init__(self, values, line_no):
        self.line_no = line_no
        self.values = values


class BinExpr(Node):
    def __init__(self, op, left, right, line_no):
        self.op = op
        self.left = left
        self.right = right
        self.line_no = line_no


class UnaryExpr(Node):
    def __init__(self, op, arg, line_no):
        self.op = op
        self.arg = arg
        self.line_no = line_no


class Assignment(Node):
    def __init__(self, var, op, value, line_no):
        self.var = var
        self.op = op
        self.value = value
        self.line_no = line_no


class BreakStatement(Node):
    def __init__(self, line_no):
        self.line_no = line_no


class ContinueStatement(Node):
    def __init__(self, line_no):
        self.line_no = line_no


class ReturnStatement(Node):
    def __init__(self, to_return, line_no):
        self.to_return = to_return
        self.line_no = line_no


class PrintStatement(Node):
    def __init__(self, to_print, line_no):
        self.to_print = to_print
        self.line_no = line_no


class RangeStatement(Node):
    def __init__(self, left, right, line_no):
        self.left = left
        self.right = right
        self.line_no = line_no


class IfStatement(Node):
    def __init__(self, condition, if_block, else_block, line_no):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
        self.line_no = line_no


class WhileLoop(Node):
    def __init__(self, condition, instructions, line_no):
        self.condition = condition
        self.instructions = instructions
        self.line_no = line_no


class ForLoop(Node):
    def __init__(self, var, for_range, instructions, line_no):
        self.var = var
        self.for_range = for_range
        self.instructions = instructions
        self.line_no = line_no


class Error(Node):
    def __init__(self, line_no):
        self.line_no = line_no


from TreePrinter import addToClass
