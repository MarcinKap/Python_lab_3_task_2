from ex2.stack import Stack


class Stack_with_searching_for_the_lowest_value(Stack):
    def __init__(self):
        Stack.__init__(self)  # constructor of base class

    def searching_lowest_number(self):
        lowest_number = self.top()
        helping_stack = Stack()
        while not self.is_empty():
            if (self.top() < lowest_number):
                lowest_number = self.top()

            x = self.top()
            helping_stack.push(x)
            y = self.pop()

        while not helping_stack.is_empty():
            self.push(helping_stack.top())
            helping_stack.pop()

        return lowest_number
