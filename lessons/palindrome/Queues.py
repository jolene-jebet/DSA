class Queue:
    capacity = 10

    def __init__(self):
        self.queue = [None] * Queue.capacity
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.queue[self.front]
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        
        answer = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)  # fixed
        self.size -= 1
        return answer
    
    def enqueue(self, e):
        if self.size == len(self.queue):
            self.resize(2 * len(self.queue))  # fixed

        avail = (self.front + self.size) % len(self.queue)  # fixed
        self.queue[avail] = e
        self.size += 1

    def resize(self, cap):
        old = self.queue
        self.queue = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.queue[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0


def is_palindrome(s):
    q = Queue()
    
    for ch in s:
        q.enqueue(ch)

    for i in range(len(s) // 2):
        front_char = q.dequeue()
        rear_char = s[len(s) - 1 - i]

        if front_char != rear_char:
            return False
    return True

# Test
print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    