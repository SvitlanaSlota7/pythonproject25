class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:

    def __init__(self):
        self.head = None  # звідси видаляємо
        self.tail = None  # сюди додаємо
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():

            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        dequeued_item = self.head.data
        self.head = self.head.next

        # Якщо після видалення черга стала порожньою, хвіст теж має бути None
        if self.head is None:
            self.tail = None

        self._size -= 1
        return dequeued_item

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "Head -> " + " -> ".join(items) + " <- Tail" if items else "Queue is empty"

if __name__ == "__main__":
    queue = LinkedQueue()

    print("Тестування додавання (enqueue)")
    queue.enqueue("Клієнт 1")
    queue.enqueue("Клієнт 2")
    queue.enqueue("Клієнт 3")
    print(queue)  # Очікуємо: Head -> Клієнт 1 -> Клієнт 2 -> Клієнт 3 <- Tail

    print("\nТестування видалення (dequeue)")
    print(f"Обслуговується: {queue.dequeue()}")
    print(queue)  # Очікуємо: Head -> Клієнт 2 -> Клієнт 3 <- Tail

    print("\nПеревірка розміру черги")
    print(f"Кількість людей у черзі: {queue.size()}")

    print("\nОчищення черги")
    queue.dequeue()
    queue.dequeue()
    print(f"Черга порожня? {queue.is_empty()}")
    print(queue)