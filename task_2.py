class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None  # Вершина стека
        self._size = 0  # Лічильник елементів

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Спроба виконати pop для порожнього стека")

        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек порожній")
        return self.top.data

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Top -> " + " -> ".join(items) if items else "Stack is empty"

if __name__ == "__main__":
    stack = LinkedStack()

    print("Тестування додавання (push)")
    stack.push("Книга 1")
    stack.push("Книга 2")
    stack.push("Книга 3")
    print(stack)  # Очікуємо: Top -> Книга 3 -> Книга 2 -> Книга 1
    print(f"Розмір стека: {stack.size()}")

    print("\nТестування перегляду (peek)")
    print(f"На вершині зараз: {stack.peek()}")

    print("\nТестування видалення (pop)")
    print(f"Вилучено: {stack.pop()}")
    print(stack)  # Очікуємо: Top -> Книга 2 -> Книга 1

    print("\nОчищення стека ")
    stack.pop()
    stack.pop()
    print(f"Стек порожній? {stack.is_empty()}")

    try:
        stack.pop()
    except IndexError as e:
        print(f"Перевірка помилки: {e}")