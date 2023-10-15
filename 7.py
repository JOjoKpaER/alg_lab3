from collections import deque

class Calculator:

    def __init__(self):
        self.stack = deque()
        self.operations = {
            '+': lambda: self.add_oper(),
            '-': lambda: self.sub_oper(),
            '*': lambda: self.mult_oper(),
            '/': lambda: self.div_oper()
        }

    def calculate(self, lst):
        if not isinstance(lst, list):
            raise Exception(str(lst) + ' was not list')
        for i in lst:
            self.readNext(i)
        return self.stack.pop()


    def readNext(self, item):
        if isinstance(item, int) or isinstance(item, float):
            self.stack.append(item)
        elif isinstance(item, str):
            try:
                operation = self.operations[item]()
            except KeyError:
                raise Exception('Cannot recognize operation:' + item)
        else:
            raise Exception('readNext recieved invalid object')
        return

    def add_oper(self):
        try:
            pop0 = self.stack.pop()
            pop1 = self.stack.pop()
            self.stack.append(pop0 + pop1)
        except Exception:
            raise Exception("Cannot perform + operation")

    def sub_oper(self):
        try:
            pop0 = self.stack.pop()
            pop1 = self.stack.pop()
            self.stack.append(pop0 - pop1)
        except Exception:
            raise Exception("Cannot perform - operation")

    def mult_oper(self):
        try:
            pop0 = self.stack.pop()
            pop1 = self.stack.pop()
            self.stack.append(pop0 * pop1)
        except Exception:
            raise Exception("Cannot perform * operation")

    def div_oper(self):
        try:
            pop0 = self.stack.pop()
            pop1 = self.stack.pop()
            self.stack.append(pop0 / pop1)
        except Exception:
            raise Exception("Cannot perform / operation")


calc = Calculator()

lst = [2, 3, '+', 4, '*']

print(calc.calculate(lst))