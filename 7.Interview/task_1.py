class Stack:

    def __init__(self, stack: list):
        self.stack = stack

    def is_empty(self):
        try:
            if self.stack[0]:
                return True
        except:
            return False

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack_ = [1, 22]
    test = Stack(stack_)
    print(test.is_empty())
    element = 'test'
    print(test.push(element))
    print(test.stack)
    print(test.pop())
    print(test.peek())
    print(test.size())
