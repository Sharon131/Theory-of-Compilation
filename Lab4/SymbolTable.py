#!/usr/bin/python
from collections import defaultdict


class Scope:

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.variables = dict()

    def put(self, name, val):
        self.variables[name] = val

    def get(self, name):
        return self.variables.get(name)


class SymbolTable(object):

    def __init__(self):
        self.current_scope = Scope(None, 'main_scope')

    def put(self, name, symbol):
        self.current_scope.put(name, symbol)

    def get(self, name):
        scope = self.current_scope
        symbol = scope.get(name)
        while scope is not None and symbol is None:
            symbol = scope.get(name)
            scope = scope.parent
        return symbol

    def getParentScope(self):
        return self.current_scope.parent

    def isInFunction(self):
        scope = self.current_scope

        while scope is not None and scope.name in ['for', 'while', 'if', 'else', 'main_scope']:
            scope = scope.parent

        return scope is not None

    def pushScope(self, name):
        self.current_scope = Scope(self.current_scope, name)

    def popScope(self):
        self.current_scope = self.current_scope.parent

