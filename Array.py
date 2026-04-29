class ArrayList:
    def __init__(self):
        self.MEMORY_SPACE = 10
        self.lastPosition = 0
        self.array = [None] * self.MEMORY_SPACE

    def get(self, position: int):
        if (position < 0 or position > (self.size() - 1)):
            raise IndexError("Index out of bounds exception")
        return self.array[position]

    def updateRemoveArray(self, start: int, end: int):
        for index in range(start, end):
            self.array[index] = self.array[index + 1]
        self.lastPosition -= 1

    def updateInsertArray(self, start: int, end: int):
        for index in range(start, end, -1):
            self.array[index] = self.array[index - 1]
        self.lastPosition += 1

    def removeAll(self):
        self.lastPosition = 0

    def add(self, value):
        if (self.lastPosition == self.capacity()):
            self.resizeMemory()
        self.array[self.lastPosition] = value
        self.lastPosition += 1

    def insertAt(self, value, position: int):
        if (position < 0 or position > self.lastPosition):
            raise IndexError("Index out of bounds exception")
        if (self.lastPosition == self.capacity()):
            self.resizeMemory()
        self.updateInsertArray(self.lastPosition, position)
        self.array[position] = value

    def removeAt(self, position: int):
        if (position < 0 or position > (self.size() - 1)):
            raise IndexError("Index out of bounds exception")
        copy = self.array[position]
        self.updateRemoveArray(position, self.size() - 1)
        return copy

    def remove(self):
        last = self.array[self.lastPosition - 1]
        self.lastPosition -= 1
        return last

    def capacity(self):
        return len(self.array)

    def size(self):
        return self.lastPosition

    def print(self):
        for position in range(0, self.lastPosition):
            print(self.array[position])

    def resizeMemory(self):
        print("Mais memoria man")
        newArray = [None] * (self.capacity() * 2)
        for position in range(self.capacity()):
            newArray[position] = self.array[position]
        self.array = newArray


class Customer:
    _counter = 1

    def __init__(self, name: str, priority: bool = False):
        self.name = name
        self.priority = priority
        self.ticket = Customer._counter
        Customer._counter += 1

    def __str__(self):
        type = "Priority" if self.priority else "Normal"
        return f"Ticket {self.ticket:03d} | {type} | {self.name}"


class BankQueue:
    def __init__(self):
        self._list = ArrayList()

    def enqueue(self, customer: Customer):
        if customer.priority:
            position = 0
            for i in range(self._list.size()):
                if self._list.get(i).priority:
                    position = i + 1
            self._list.insertAt(customer, position)
        else:
            self._list.add(customer)

    def dequeue(self) -> Customer:
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self._list.removeAt(0)

    def peek(self) -> Customer:
        if self.isEmpty():
            raise IndexError("Queue is empty.")
        return self._list.get(0)

    def isEmpty(self) -> bool:
        return self._list.size() == 0

    def size(self) -> int:
        return self._list.size()

    def print(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self._list.size()):
            customer = self._list.get(i)
            next = " <- next" if i == 0 else ""
            print(f"  [{i}] {customer}{next}")


if __name__ == "__main__":
    queue = BankQueue()

    # isEmpty() verifica se a fila esta vazia
    print("isEmpty()")
    print(f"Queue is empty: {queue.isEmpty()}")

    # enqueue() adiciona clientes normais e prioritarios
    print("\n enqueue()")
    queue.enqueue(Customer("Ana Silva"))
    queue.enqueue(Customer("Bruno Costa"))
    queue.enqueue(Customer("Carla Dias"))
    queue.enqueue(Customer("Daniel Souza", priority=True))
    queue.enqueue(Customer("Elisa Nunes",  priority=True))


    # print() exibe todos os clientes da fila
    print("\n print()")
    queue.print()

    # size() retorna o total de clientes na fila
    print("\n size()")
    print(f"Customers in queue: {queue.size()}")

    # peek() consulta o proximo sem remover
    print("\n peek()")
    print(f"Next customer: {queue.peek()}")

    # dequeue() atende (remove) o proximo da fila
    print("\n dequeue()")
    print(f"Serving: {queue.dequeue()}")
    print(f"Serving: {queue.dequeue()}")

    print("\n Queue after 2 dequeues:")
    queue.print()

    # isEmpty() checando novamente apos remocoes
    print("\n isEmpty() after dequeues")
    print(f"Queue is empty: {queue.isEmpty()}")

    # dequeue() esvaziando o restante
    print("\n dequeue() until empty")
    while not queue.isEmpty():
        print(f"Serving: {queue.dequeue()}")

    print(f"\nQueue is empty: {queue.isEmpty()}")

    # dequeue() em fila vazia - deve lancar excecao
    print("\n dequeue() on empty queue (exception)")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}")

    # peek() em fila vazia - deve lancar excecao
    print("\n peek() on empty queue (exception)")
    try:
        queue.peek()
    except IndexError as e:
        print(f"Error caught: {e}")