
import AST
import SymbolTable
from Memory import *
from Exceptions import *
from visit import *
import sys
import numpy
from collections import defaultdict
import typing

sys.setrecursionlimit(10000)

ffun_bin = defaultdict(lambda first_arg, second_arg: typing.Any)

ffun_bin['+'] = lambda first, second: first + second
ffun_bin['-'] = lambda first, second: first - second
ffun_bin['*'] = lambda first, second: first * second
ffun_bin['/'] = lambda first, second: first / second

ffun_bin['<'] = lambda first, second: first < second
ffun_bin['>'] = lambda a, b: a > b
ffun_bin['=='] = lambda a, b: a == b
ffun_bin['!='] = lambda a, b: a != b
ffun_bin['<='] = lambda a, b: a <= b
ffun_bin['>='] = lambda a, b: a >= b

ffun_unary = defaultdict(lambda arg: typing.Any)

ffun_unary['-'] = lambda arg: -arg
ffun_unary['\''] = lambda arg: numpy.transpose(arg)
ffun_unary["ONES"] = lambda arg: numpy.ones(arg)
ffun_unary["ZEROS"] = lambda arg: numpy.zeros(arg)
ffun_unary["EYE"] = lambda arg: numpy.eye(arg)


class Interpreter(object):

    def __init__(self):
        self.memory_stack = MemoryStack(Memory('global'))

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)
            # self.visit(instruction)

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.Variable)
    def visit(self, node):
        return self.memory_stack.get(node.name)

    @when(AST.Submatrix)
    def visit(self, node):
        var = node.var.accept(self)
        indices = node.vector.accept(self)
        return var[indices]

    @when(AST.Vector)
    def visit(self, node):
        to_return = []
        for elem in node.values:
            to_return.append(elem.accept(self))
        return to_return

    @when(AST.BinExpr)
    def visit(self, node):
        first = node.left.accept(self)
        second = node.right.accept(self)

        op = node.op
        if node.op[0] == '.':
            op = node.op[1:]

        return ffun_bin[op](first, second)

    @when(AST.UnaryExpr)
    def visit(self, node):
        val = node.arg.accept(self)
        return ffun_unary[node.op](val)

    @when(AST.CreateMatrix)
    def visit(self, node):
        val = node.arg.accept(self)
        return ffun_bin[node.op](val)

    @when(AST.Assignment)
    def visit(self, node):
        value = node.value.accept(self)
        # modifying assignment
        if node.op[0] != '=':
            curr_val = node.var.accept(self)
            self.memory_stack.set(node.var.name, ffun_bin[node.op[0]](curr_val, value))
        else:
            if isinstance(node.var, AST.Submatrix):
                var = node.var.var.accept(self)
                indices = node.var.vector.accept(self)
                value = node.value.accept(self)
                var[indices] = value
            else:
                self.memory_stack.insert(node.var.name, value)

    @when(AST.BreakStatement)
    def visit(self, node):
        raise BreakException

    @when(AST.ContinueStatement)
    def visit(self, node):
        raise ContinueException

    @when(AST.ReturnStatement)
    def visit(self, node):
        pass

    @when(AST.PrintStatement)
    def visit(self, node):
        for arg in node.to_print:
            print(arg.accept(self), end=" ")
        print("")

    @when(AST.RangeStatement)
    def visit(self, node):
        val1 = node.left.accept(self)
        val2 = node.right.accept(self)
        return range(val1, val2)

    @when(AST.IfStatement)
    def visit(self, node):
        self.memory_stack.push(Memory('if'))
        if node.condition.accept(self):
            node.if_block.accept(self)  # check if its one instruction or list of them in Instructions class
        elif node.else_block is not None:
            node.else_block.accept(self)  # should actually be ok

    # simplistic while loop interpretation
    @when(AST.WhileLoop)
    def visit(self, node):
        self.memory_stack.push(Memory("while"))
        r = None
        try:
            while node.condition.accept(self):
                try:
                    r = node.instructions.accept(self)
                except ContinueException:
                    pass
        except BreakException:
            pass
        finally:
            self.memory_stack.pop()
        return r

    @when(AST.ForLoop)
    def visit(self, node):
        self.memory_stack.push(Memory("for"))
        r = None
        self.memory_stack.insert(node.var.name, node.for_range.left)
        try:
            for x in node.for_range.accept(self):
                try:
                    self.memory_stack.set(node.var.name, x)
                    r = node.instructions.accept(self)
                except ContinueException:
                    pass
        except BreakException:
            pass
        finally:
            self.memory_stack.pop()
        return r

