class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Додаємо елемент у кінець черги"""
        self._items.insert(0, item)

    def dequeue(self):
        """Видаляємо та повертаємо перший елемент черги."""
        if not self.is_empty():
            return self._items.pop()
        return None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        """Повертаємо кількість елементів."""
        return len(self._items)

    def get_from_queue(self, e):

        found_element = None
        initial_size = self.size()

        for _ in range(initial_size):
            current = self.dequeue()

            # Знайшли елемент і ще не вилучали його в цьому циклі
            if current == e and found_element is None:
                found_element = current
                continue

                # Якщо це не той елемент, повертаємо його в кінець черги
            self.enqueue(current)

        if found_element is None:
            raise ValueError(f"Елемент '{e}' не знайдено в черзі.")

        return found_element

    def __str__(self):
        """Відображення черги зліва направо: від початку до кінця"""
        return f"Queue (head -> tail): {list(reversed(self._items))}"

if __name__ == "__main__":
    my_queue = Queue()

    for char in ['A', 'B', 'C', 'D', 'E']:
        my_queue.enqueue(char)

    print("Початковий стан:", my_queue)

    try:
        element = my_queue.get_from_queue('C')
        print(f"\nЗнайдено та вилучено: {element}")
        print("Після вилучення 'C':", my_queue)
    except ValueError as err:
        print(f"Помилка: {err}")

    try:
        print("\nШукаємо елемент 'Z'...")
        my_queue.get_from_queue('Z')
    except ValueError as err:
        print(f"Результат перевірки: {err}")

    print("\nПоточний початок черги:", my_queue.dequeue())
    print("Стан після виходу першого елемента:", my_queue)