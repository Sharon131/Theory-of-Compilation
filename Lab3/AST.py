
class Node(object):
    pass


class Program(Node):
    def __init__(self, value):
        self.value = value


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


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg


class BreakStatement(Node):
    def __init__(self, name):
        self.name = name


class ContinueStatement(Node):
    def __init__(self, name):
        self.name = name


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


class RangeStatement(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class IfStatement(Node):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block


class WhileLoop(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction


class ForLoop(Node):
    def __init__(self, var, range, instruction):
        self.var = var
        self.range = range
        self.instruction = instruction


class Error(Node):
    def __init__(self):
        pass
