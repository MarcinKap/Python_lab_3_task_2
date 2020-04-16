from ex2.stack import Stack
from ex2.stack.finding_number import Stack_with_searching_for_the_lowest_value


def main():
    stack = Stack_with_searching_for_the_lowest_value()
    stack.push(5)
    stack.push(2)
    stack.push(3)
    stack.push(50)
    stack.push(4)

    print('najniższy numer to:', end = ' ')
    print(stack.searching_lowest_number())

    print('wypiywanie stosu:')
    while not stack.is_empty():
        print(stack.top(), end=' ')
        stack.pop()

if '__main__' == __name__:
    main()
