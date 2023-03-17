from collections import deque
import sys

def push_front(x, deque):
    deque.appendleft(x)
    
def push_back(x, deque):
    deque.append(x)
    
def pop_front(deque):
    if len(deque) > 0:
        print(deque.popleft())
    else:
        print(-1)

def pop_back(deque):
    if len(deque) > 0:
        print(deque.pop())
    else:
        print(-1)
        
def size(deque):
    print(len(deque))
    
def empty(deque):
    if len(deque) == 0:
        print(1)
    else:
        print(0)

def front(deque):
    if len(deque) > 0:
        print(deque[0])
    else:
        print(-1)

def back(deque):
    if len(deque) > 0:
        print(deque[-1])
    else:
        print(-1)


n = int(input())

deque = deque()

for _ in range(n):
    
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == "push_front":
        push_front(int(cmd[-1]), deque)
    
    elif cmd[0] == "push_back":
        push_back(int(cmd[-1]), deque)
    
    elif cmd[0] == "pop_front":
        pop_front(deque)
        
    elif cmd[0] == "pop_back":
        pop_back(deque)
        
    elif cmd[0] == "size":
        size(deque)
        
    elif cmd[0] == "empty":
        empty(deque)
        
    elif cmd[0] == "front":
        front(deque)
        
    elif cmd[0] == "back":
        back(deque)