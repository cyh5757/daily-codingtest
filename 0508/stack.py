class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            print(f"Popped: {self.items.pop()}")
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            print(f"Top: {self.items[-1]}")
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# 명령어 입력
stack = Stack()
print("명령어 예시: push 10, pop, peek, size, exit")

while True:
    command = input(">> ").strip().split()

    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "peek":
        stack.peek()
    elif command[0] == "size":
        print("Size:", stack.size())
    elif command[0] == "exit":
        print("종료합니다.")
        break
    else:
        print("알 수 없는 명령입니다.")
