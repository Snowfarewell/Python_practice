class Stack:
  """스택 클래스입니다."""

  def __init__(self):
    """빈 스택을 생성합니다."""
    self._data = []

  def __len__(self):
    """스택에 저장된 요소의 개수를 반환합니다."""
    return len(self._data)

  def push(self, element):
    """스택에 요소를 추가합니다."""
    self._data.append(element)

  def is_empty(self):
    """스택이 비어있는지 확인합니다."""
    return len(self._data) == 0

  def pop(self):
    """스택의 최상단 요소를 반환하고 제거합니다."""
    if self.is_empty():
      raise Exception("스택이 비어 있습니다.")
    return self._data.pop()

  def top(self):
    """스택의 최상단 요소를 반환합니다."""
    if self.is_empty():
      raise Exception("스택이 비어 있습니다.")
    return self._data[-1]


# 스택 사용 예시
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3 출력
print(stack.pop())  # 2 출력
print(stack.pop())  # 1 출력
print(stack.is_empty())  # True 출력
