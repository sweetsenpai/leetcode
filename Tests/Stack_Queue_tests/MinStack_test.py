import pytest
from Stack_Queue.MinStack import MinStack


def test_min_stack():
    # Создаём объект MinStack
    stack = MinStack()

    # Проверяем push и getMin
    stack.push(5)
    assert stack.getMin() == 5

    stack.push(3)
    assert stack.getMin() == 3

    stack.push(7)
    assert stack.getMin() == 3

    # Проверяем top
    assert stack.top() == 7

    # Проверяем pop
    stack.pop()
    assert stack.getMin() == 3

    stack.pop()
    assert stack.getMin() == 5

    # Проверяем дубликаты
    stack.push(2)
    stack.push(2)
    assert stack.getMin() == 2

    stack.pop()
    assert stack.getMin() == 2

    stack.pop()
    assert stack.getMin() == 5
