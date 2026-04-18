class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        return None

    def is_empty(self):
        """Перевірка чи порожній стек."""
        return len(self._items) == 0

    def get_from_stack(self, e):
        temp_stack = []
        found_element = None

        # Перекладаємо елементи у тимчасовий список, поки не знайдемо 'e'
        while not self.is_empty():
            current = self.pop()
            if current == e:
                found_element = current
                break
            temp_stack.append(current)

        # Повертаємо всі елементи з тимчасового списку назад у стек
        while temp_stack:
            self.push(temp_stack.pop())

        if found_element is None:
            raise ValueError(f"Елемент '{e}' не знайдено у стеку.")

        return found_element

    def __str__(self):
        return f"Stack: {self._items}"


# --- ПЕРЕВІРКА ЗАВДАННЯ НА ПРИКЛАДАХ ---

if __name__ == "__main__":
    my_stack = Stack()

    # Наповнюємо стек
    for x in [10, 20, 30, 40, 50]:
        my_stack.push(x)

    print("Початковий стан:", my_stack)

    # Приклад 1: Успішний пошук елемента в середині
    try:
        element = my_stack.get_from_stack(30)
        print(f"\nЗнайдено та вилучено: {element}")
        print("Стан після вилучення 30:", my_stack)
    except ValueError as err:
        print(f"Помилка: {err}")

    # Приклад 2: Пошук елемента, якого немає
    try:
        print("\nШукаємо число 100...")
        my_stack.get_from_stack(100)
    except ValueError as err:
        print(f"Результат перевірки: {err}")

    # Приклад 3: Стан стека після помилкового пошуку (має бути без змін)
    print("Стан стека після невдалого пошуку:", my_stack)