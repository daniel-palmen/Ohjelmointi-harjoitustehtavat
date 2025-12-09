class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        new_node = Node(data)
        self._size += 1
        if self._top is None:
            self._top = new_node
        else:
            previous_node = self._top
            new_node.next = previous_node
            self._top = new_node
        return

    def pop(self):
        if self._size == 0:
            return None
        pop_node = self._top
        val = pop_node.data
        freshTop_node = pop_node.next
        del(pop_node)
        self._top = freshTop_node
        self._size -= 1
        return val

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

def check_balance(text):
    # set counter
    S = 0
    # position counter
    C = 0
    # boolean check
    boo = 0
    # create stack
    mystack = Stack()
    for char in text:
        if char in ("(","[","{"):
            mystack.push(char)
            boo = 1
        elif char ==")":
            if mystack.peek() == "(":
                mystack.pop()
                S += 1
                boo = 0
            else:
                return f'Match error at position {C}'
        elif char =="]":
            if mystack.peek() == "[":
                mystack.pop()
                S += 1
                boo = 0
            else:
                return f'Match error at position {C}'
        elif char =="}":
            if mystack.peek() == "{":
                mystack.pop()
                S += 1
                boo = 0
            else:
                return f'Match error at position {C}'
        C += 1
    if boo == 0:
        return f'Match error at position {C-1}'
    text = f'Ok - {S}'
    return text

test = check_balance(r'a(b)c[d]e{f}g')
print(test)