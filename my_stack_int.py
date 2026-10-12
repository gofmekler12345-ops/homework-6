class MyStackInt:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, num):
        self._stack.append(num)
        if not self._max_stack or num >= self._max_stack[-1]:
            self._max_stack.append(num)
        else:

            self._max_stack.append(self._max_stack[-1])

    def pop(self):
        if not self._stack:
            return  "pop from empty stack"
        self._max_stack.pop()
        return self._stack.pop()

    def max(self):
        if not self._max_stack:
            raise IndexError("max from empty stack")
        return self._max_stack[-1]