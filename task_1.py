class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("Спроба отримати елемент з порожнього стека")

def reverse_string(input_text):
    stack = Stack()

    # Кожен символ рядка розміщаємо у стек
    for char in input_text:
        stack.push(char)

    reversed_text = ""

    #  Символи зі стека вибираємо, поки він не стане порожнім
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text

if __name__ == "__main__":
    user_input = input("Введіть послідовність символів ")
    result = reverse_string(user_input)

    print(f"Оригінал: {user_input}")
    print(f"Реверс:   {result}")