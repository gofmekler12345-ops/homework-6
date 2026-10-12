from unittest import TestCase, main
from my_stack_int import MyStackInt


class TestMyStackInt(TestCase):

    def test_push_and_max(self):
        stack = MyStackInt()
        stack.push(3)
        self.assertEqual(stack.max(), 3)
        stack.push(5)
        self.assertEqual(stack.max(), 5)
        stack.push(2)
        self.assertEqual(stack.max(), 5)
        stack.push(5)
        self.assertEqual(stack.max(), 5)

    def test_pop_and_max_changes(self):
        stack = MyStackInt()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.max(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.max(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.max(), 1)


if __name__ == "__main__":
    main()