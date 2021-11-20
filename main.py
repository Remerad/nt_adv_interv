class Stack(object):
    stack_list = []

    def __init__(self, *args):
        self.push(args)
        pass

    def isEmpty(self):
        """проверка стека на пустоту. Метод возвращает True или False."""
        if len(self.stack_list):
            return False
        else:
            return True

    def push(self, *args):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        for a in list(args):
            self.stack_list.extend(a)

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

    def isBalanced(self):
        round_bracket_counter = 0
        square_bracket_counter = 0
        curly_bracket_counter = 0

        while not self.isEmpty():
            temp = self.pop()
            if temp == "(":
                round_bracket_counter += 1
            if temp == ")":
                round_bracket_counter -= 1
                if round_bracket_counter > 0:
                    break
            if temp == "[":
                square_bracket_counter += 1
            if temp == "]":
                square_bracket_counter -= 1
                if square_bracket_counter > 0:
                    break
            if temp == "{":
                curly_bracket_counter += 1
            if temp == "}":
                curly_bracket_counter -= 1
                if curly_bracket_counter > 0:
                    break
        if abs(round_bracket_counter) + abs(square_bracket_counter) + abs(curly_bracket_counter):
            return "Несбалансированно"
        else:
            return "Сбалансированно"


if __name__ == '__main__':
    # print('Начали')
    # st = Stack()
    # print(st.isEmpty())
    # st.print_all()
    # st.push(9)
    # st.print_all()
    # print(st.pop())
    # st.print_all()
    # print(st.peek())
    # st.print_all()
    # print(st.size())
    # st.print_all()


    st = Stack()
    st.push(list(input("Введите строку со скобками: ")))
    print(st.isBalanced())


