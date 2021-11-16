class Stack(object):
    stack_list = []

    def __init__(self, *args):
        self.stack_list.extend(args)
        pass

    def isEmpty(self):
        """проверка стека на пустоту. Метод возвращает True или False."""
        if len(self.stack_list):
            return False
        else:
            return True

    def push(self, a):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        self.stack_list.append(a)

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."""
        return self.stack_list.pop()

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""
        return self.stack_list[-1]

    def size(self):
        """возвращает количество элементов в стеке."""
        return len(self.stack_list)

    def print_all(self):
        print(self.stack_list)
        pass


if __name__ == '__main__':
    print('Начали')
    st = Stack(1, 2, 4)
    print(st.isEmpty())
    st.print_all()
    st.push(9)
    st.print_all()
    print(st.pop())
    st.print_all()
    print(st.peek())
    st.print_all()
    print(st.size())
    st.print_all()