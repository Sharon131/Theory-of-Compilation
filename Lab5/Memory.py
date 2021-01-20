
class Memory:

    def __init__(self, name, parent=None):  # memory name
        self.vars = dict()
        self.name = name

    def has_key(self, name):  # variable name
        if name in self.vars:
            return True
        else:
            return False

    def get(self, name):         # gets from memory current value of variable <name>
        if name in self.vars:
            return self.vars[name]
        else:
            return None

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.vars[name] = value


class MemoryStack:

    def __init__(self, memory=None):  # initialize memory stack with memory <memory>
        self.stack = []
        self.size = 0
        if memory is not None:
            self.push(memory)

    def get(self, name):             # gets from memory stack current value of variable <name>
        for i in reversed(range(self.size)):
            if self.stack[i].has_key(name):
                return self.stack[i].get(name)
        return None
        # iterate over all stack to find that variable

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stack[self.size-1].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        for i in reversed(range(self.size)):
            if self.stack[i].has_key(name):
                self.stack[i].put(name, value)
                return True
        return False

    def push(self, memory): # pushes memory <memory> onto the stack
        self.stack.append(memory)
        self.size += 1

    def pop(self):          # pops the top memory from the stack
        self.size -= 1
        return self.stack.pop()


