class Stack:
    def __init__(self):
        self.stack = []
    
    def length(self) -> int:
        return len(self.stack)
    
    def isEmpty(self) -> bool:
        return self.length() == 0
    
    def push(self,data) -> None:
        self.stack.append(data)

    def top(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        
        return self.stack.pop()

def PalindromeChecker(word:str) -> bool:
    stack:Stack = Stack()
    checker:bool = True
    index:int = 0

    for letter in word:
        stack.push(letter)

    while stack.length() > 0:
        letter = stack.pop()

        if letter != word[index]:
            checker = False
            break

        index += 1

    return checker

print(PalindromeChecker("racecar"))