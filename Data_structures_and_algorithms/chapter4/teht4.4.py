class Queue():
    def __init__(self):
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = self._OutboundStack + self._InboundStack [::-1]
        return (
        f'<Queue ({self._size} element{plural}): '
        f'[{", ".join(values)}]>'
        )

    def enqueue(self, data):
        self._size += 1
        self._InboundStack.append(data)

    def dequeue(self):
        if self._size == 0:
            return None

        if not self._OutboundStack:
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())

        self._size -= 1
        return self._OutboundStack.pop()