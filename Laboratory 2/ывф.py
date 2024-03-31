from collections import deque


class LinkedNode:
    def init(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Stack:
    def init(self):  # инициализация
        self.head = LinkedNode()
        self.size = 0

    def is_empty(self):  # is_empty - определить, пусто ли оно
        return self.size == 0

    def push(self, value):  # push - добавляет элемент в верхнюю часть стека (стекийн дээд хэсэгт элемент нэмнэ)
        if self.len() > 0:
            node = LinkedNode(value)
            node.right = self.head
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop(self):  # pop - удаляет элемент в верхней части стека
        if self.is_empty():
            return print("Стек пуст")
        remove = self.head
        if self.size > 1:
            self.head = remove.right
        self.size -= 1
        return remove.value

    def len(self):  # возвращает количество элементов в стеке
        return self.len(self)


# Дек     Deque - это двусторонняя очередь, которая позволяет эффективно вставлять и удалять элементы с обоих концов.
class Deque:
    def init(self):  # инициализация
        self.head = LinkedNode()
        self.tail = self.head
        self.size = 0

    def is_empty(self):  # is_empty - определить, пусто ли оно
        return self.size == 0

    def push_left(self, value):  # добавляет к началу двухсторонней очереди
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.tail
            self.tail.left = node
            self.tail = node
        else:
            self.tail.value = value
        self.size += 1

    def push(self, value):  # добавляет к концу двухсторонней очереди
        if self.size > 0:
            node = LinkedNode(value)
            node.left = self.head
            self.head.right = node
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop_left(self):  # удаляет и возвращает элемент с левой стороны двусторонней очереди
        if self.is_empty():
            return print("Стек пуст")
        remove = self.tail
        if self.size > 1:
            self.tail = remove.right
        self.size -= 1
        return remove.value

    def pop(self):  # удаляет и возвращает элемент с правой стороны двусторонней очереди
        if self.is_empty():
            return print("Стек пуст")
        remove = self.head
        if self.size > 1:
            self.head = remove.left
        self.size -= 1
        return remove.value

    def len(self):  # возвращает количество элементов в двухсторонней очереди
        return self.size
s = Stack()
s.push(1)
print(s.is_empty())
print(s.pop())

d = Deque()
print(d.is_empty())
d.push(2)
d.push_left(3)
d.push(4)
print(d.pop())
print(d.pop_left())


def task1():
    file = open("Books.txt")
    jtr = file.read().split(", ")

    deq1 = deque()
    deq2 = deque()
    for i in jtr:
        deq1.append(i)
    deq2.append(deq1.popleft())

    k = deq1.popleft()
    s = deq2.pop()

    if k > s:
        deq2.append(s)
        deq2.append(k)
    else:
        deq2.append(k)
        deq2.append(s)

    while deq1:
        k = deq1.popleft()
        s = deq2.pop()
        while k < s:
            deq1.append(s)
            s = deq2.pop()
            if len(deq2) == 0:
                break
        deq2.append(min(k,s))
        deq2.append(max(k,s))

    print(deq2)

def task2():
    file = open("Shivrovka.txt")
    jtr = file.read()
    deq = deque()
    for i in jtr:
        deq.append(i)


    while deq:
        s = deq.popleft()
        if s == 'A':
            print("Y",end='')
        elif s ==  'B':
            print("Z", end='')
        else:
            print(chr(ord(s)-2))


def hanoi2(n, source, auxiliary, target):
    if n > 0:
        # Перемещение n-1 дисков с source на auxiliary
        hanoi2(n - 1, source, target, auxiliary)

        # Перемещение самого большого диска с source на target
        target.append(source.pop())

        # Перемещение n-1 дисков с auxiliary на target
        hanoi2(n - 1, auxiliary, source, target)

def hanoi1():
    s1 = []
    s2 = []
    s3 = []
    file = open("3task.txt")
    k = file.read()
    lis = list(map(int,k.split(' ')))
    for i in lis:
        s1.append(i)

    hanoi2(12, s1, s2, s3)


def check_brackets():
    file = open("skobki.txt")
    s = file.read()

    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                print("Баланс не соблюден")
                return False
    if len(stack) == 0:
        print("Баланс соблюден")
    else:
        print("Баланс не соблюден")


def check_brackets2():
    file = open("skobki2.txt")
    s = file.read()

    stack = []
    for char in s:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                print("Баланс не соблюден")
                return False
    if len(stack) == 0:
        print("Баланс соблюден")
    else:
        print("Баланс не соблюден")


def print_characters():
    digits = []
    letters = []
    others = []
    file = open("charactes.txt")
    s = file.read()

    for char in s:
        if char.isdigit():
            digits.append(char)
        elif char.isalpha():
            letters.append(char)
        else:
            others.append(char)

    print("Цифры:", end = " ")
    while digits:
        print(digits.pop(), end = " ")
    print("\n")
    print("Буквы:", end = " ")
    while letters:
        print(letters.pop(), end=" ")
    print("\n")
    print("Остальные символы:", end = " ")
    while others:
        print(others.pop(), end=" ")


def task7():
    c = 0
    deq = deque()
    file = open("chisla.txt")
    s = list(map(int, file.read().split(" ")))
    for i in range(len(s)-1, -1, -1):
        if s[i] > 0:
            deq.appendleft(s[i])
            c +=1
        else:
            deq.append(s[i])
    print(deq)
    for i in range(c):
        print(deq.pop(), end = " ")
    while deq:
        print(deq.popleft(), end = " ")

def task8():
    file = open('read.txt')
    s = file.readlines()
    stack = []
    for i in s:
        stack.append(i[:-1])
    while stack:
        print(stack.pop())
