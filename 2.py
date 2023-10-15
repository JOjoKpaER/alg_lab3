class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

###########################################################################

    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(Node(item))

    def index(self, item):
        if self.isEmpty():
            raise Exception("List is empty")
        current = self.head
        found = False
        index = 0
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1

        if current is None:
            index = -1

        return index

    def insert(self, pos, item):
        if self.isEmpty():
            raise Exception("List is empty")
        if pos >= self.size():
            raise Exception("pos: " + str(pos) + " was greater than size: " + str(self.size()))
        if pos == 0:
            prev = self.head
            self.head = Node(item)
            self.head.setNext(prev)
            return
        index = 0
        current = self.head
        while index != pos - 1:
            current = current.getNext()
            index += 1
        next_ = current.getNext()
        current.setNext(Node(item))
        current.getNext().setNext(next_)

    def pop(self, pos=None):
        if pos is not None and not isinstance(pos, int):
            raise Exception("pos: " + str(type(pos)) + " was not int")
        if self.isEmpty():
            raise Exception("List is empty")
        if self.head.getNext() is None:
            ret = self.head.getData()
            del self.head
            return ret
        current = self.head.getNext()
        prev = self.head
        if pos is not None:
            if pos == 0:
                ret = prev.getData()
                del prev
                self.head = current
                return ret
            if pos == 1:
                ret = current.getData()
                prev.setNext(current.getNext())
                del current
                return ret
            index = 0
            while index != pos - 1:
                prev = current
                current = current.getNext()
                index += 1
            ret = current.getData()
            next_ = current.getNext()
            del current
            prev.setNext(next_)
            return ret
        else:
            while current.getNext():
                prev = current
                current = current.getNext()
            ret = current.getData()
            del current
            prev.setNext(None)
            return ret

    def __str__(self):
        ret = '['
        if self.isEmpty():
            return ret + ']'
        current = self.head
        while current.getNext() is not None:
            ret += str(current.getData()) + ', '
            current = current.getNext()
        ret += str(current.getData())
        return ret + "]"

    def slice(self, start, stop):
        if self.isEmpty():
            raise Exception("List is empty")
        ret = []
        for i in range(stop - start):
            ret.append(self.pop(start + i))
        return ret


def move_to_front():
    ulist = UnorderedList()

    while True:
        inpt = input()
        if inpt == '':
            break
        if not ulist.search(inpt):
            ulist.append(inpt)
        else:
            ulist.pop(ulist.index(inpt))
            ulist.append(inpt)
        print(str(ulist))


move_to_front()


