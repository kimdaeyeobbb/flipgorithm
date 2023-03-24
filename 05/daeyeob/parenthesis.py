# 스택 구현
class Stack:
    def __init__(self):  # 생성자 함수 (인스턴스를 만들때 처음 호출) - 첫 매개변수로 반드시 self를 지정. 인스턴스(객체)의 초기화 진행
        self.container = list() # self.속성 = 값. 데이터를 담을 객체는 동적 배열

    def empty(self): # self에 인스턴스가 전달됨
        if not self.container:   # 데이터를 담을 객체가 비어있다면
            return True
        else:   # 데이터를 담을 객체가 비어있지 않다면
            return False

    def push(self, data):
        self.container.append(data)  # 스택의 top에 요소추가 (배열의 맨 마지막에 추가)

    def pop(self):
        if self.empty():  # 리스트가 비어있다면
            return None  # pop 할것이 없음
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        return self.container[-1]  # 스택 상 top요소


t = int(input())  # t: 입력 데이터 수

for _ in range(t):
    parenthesis = list(input())
    s = Stack()  # 클래스를 변수에 담아서 사용

    for element in parenthesis:
        if element == "(":
            s.push(element)
        elif element == ")":
           if not s.empty():
               s.pop()
           else:
               print("NO")
               break
    else:  # break하지 않고 끝까지 왔을 경우
        print("YES") if s.empty() else print("NO")



'''
* 클래스의 장점
- 재사용성 증가
- 코드의 수정 최소화

* __init__ 참고자료
https://wikidocs.net/89
https://dojang.io/mod/page/view.php?id=2373
'''


'''
* 스택
- OS가 관리하는 메모리 영역 중 지역 변수가 할당되는 스택 메모리에 스택 프레임이 쌓임
- 트리에서 모든 데이터를 순회할 때 스택을 사용
'''