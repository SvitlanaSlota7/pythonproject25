class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """Додає елемент у початок списку операція O(1)"""
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Додає елемент у кінець списку O(n)."""
        temp = Node(item)
        if self.is_empty():
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    def index(self, item):
        """Повертає позицію елемента. Якщо не знайдено — ValueError."""
        current = self.head
        pos = 0
        while current is not None:
            if current.data == item:
                return pos
            current = current.next
            pos += 1
        raise ValueError(f"'{item}' is not in list")

    def insert(self, pos, item):
        """Вставляє елемент на вказану позицію."""
        if pos <= 0:
            self.add(item)
            return

        temp = Node(item)
        current = self.head
        previous = None
        current_pos = 0

        while current is not None and current_pos < pos:
            previous = current
            current = current.next
            current_pos += 1

        temp.next = current
        if previous is not None:
            previous.next = temp

    def pop(self, pos=None):
        """Видаляє та повертає останній елемент"""
        if self.is_empty():
            raise IndexError("pop from empty list")

        # Якщо позиція не вказана, видаляємо останній
        if pos is None:
            pos = self.size() - 1

        current = self.head
        previous = None
        current_pos = 0

        while current.next is not None and current_pos < pos:
            previous = current
            current = current.next
            current_pos += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def slice(self, start, stop):
        """Повертає копію списку від start до stop (не включаючи stop)."""
        new_list = UnsortedList()
        current = self.head
        current_pos = 0

        # Для збереження порядку при додаванні в копію використаємо список
        temp_data = []

        while current is not None and current_pos < stop:
            if current_pos >= start:
                temp_data.append(current.data)
            current = current.next
            current_pos += 1

        # Додаємо в новий список у зворотному порядку, щоб зберегти черговість
        for item in reversed(temp_data):
            new_list.add(item)

        return new_list

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(items) + "]"

if __name__ == "__main__":
    mylist = UnsortedList()

    print("1. Тест append:")
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    print(mylist)  # [10 -> 20 -> 30]

    print("\n2. Тест index:")
    print(f"Індекс числа 20: {mylist.index(20)}")

    print("\n3. Тест insert (вставляємо 15 на позицію 1):")
    mylist.insert(1, 15)
    print(mylist)  # [10 -> 15 -> 20 -> 30]

    print("\n4. Тест pop (видаляємо останній):")
    print(f"Видалено: {mylist.pop()}")
    print(mylist)  # [10 -> 15 -> 20]

    print("\n5. Тест slice (від 0 до 2):")
    sublist = mylist.slice(0, 2)
    print(f"Оригінал: {mylist}")
    print(f"Слайс:    {sublist}")