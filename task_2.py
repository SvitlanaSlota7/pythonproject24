class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self._items) == 0

    def peek(self):
        return self._items[-1] if not self.is_empty() else None


def is_balanced(sequence):
    stack = Stack()
    # Відповідність закритих дужок відкритим
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            # Стек порожній або верхній елемент не збігається — не збалансовано
            if stack.is_empty() or stack.pop() != brackets_map[char]:
                return False

    # Стек порожній — все збалансовано
    return stack.is_empty()

test_cases = ["{[()]}", "{[(])}", "{{[[(())]]}}", "((()))", "(()"]

for tc in test_cases:
    print(f"{tc}: {'Balanced' if is_balanced(tc) else 'Not balanced'}")