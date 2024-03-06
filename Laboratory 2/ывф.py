from collections import deque

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


def hanoi(n, source, auxiliary, target):
    if n > 0:
        # Перемещение n-1 дисков с source на auxiliary
        hanoi(n - 1, source, target, auxiliary)

        # Перемещение самого большого диска с source на target
        target.append(source.pop())
        print("Переместить диск", n, "с", source, "на", target)

        # Перемещение n-1 дисков с auxiliary на target
        hanoi(n - 1, auxiliary, source, target)

"""
s1 = []
s2 = []
s3 = []
file = open("3task.txt")
k = file.read()
lis = list(map(int,k.split(' ')))
for i in lis:
    s1.append(i)

hanoi(12, s1, s2, s3)
"""

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

    print("Цифры:", ''.join(digits))
    print("Буквы:", ''.join(letters))
    print("Остальные символы:", ''.join(others))


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
print_characters()