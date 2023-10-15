class Node:

    def __init__(self, item, prev=None, next_=None):
        self.item = item
        self.prev = prev
        self.next = next_


class DoubleList:

    def __init__(self):
        self.current = None

    def is_empty(self):
        return self.current is None

    def search(self, item):
        if self.is_empty():
            return
        if self.current.next is None:
            while self.current.prev is not None:
                if self.current.item == item:
                    return True
                self.current = self.current.prev
            return False
        if self.current.prev is None:
            while self.current.next is not None:
                if self.current.item == item:
                    return True
                self.current = self.current.next
            return False

    def size(self):
        size = 0
        if self.is_empty():
            return size
        if self.current.next is None:
            while self.current.prev is not None:
                self.current = self.current.prev
                size += 1
            return size
        if self.current.prev is None:
            while self.current.next is not None:
                self.current = self.current.next
                size += 1
            return size

    def add_start(self, item):
        if self.is_empty():
            self.current = Node(item)
            return
        while self.current.prev is not None:
            self.current = self.current.prev
        self.current.prev = Node(item, None, self.current)
        self.current = self.current.prev

    def add_end(self, item):
        if self.is_empty():
            self.current = Node(item)
            return
        while self.current.next is not None:
            self.current = self.current.next
        self.current.next = Node(item, self.current, None)
        self.current = self.current.next

    def pop_start(self):
        if self.is_empty():
            return None
        if self.size() == 1:
            ret = self.current.item
            del self.current
            return ret
        while self.current.prev is not None:
            self.current = self.current.prev
        ret = self.current.item
        next_ = self.current.next
        del self.current
        self.current = next_
        return ret

    def pop_end(self):
        if self.is_empty():
            return None
        if self.size() == 1:
            ret = self.current.item
            del self.current
            return ret
        while self.current.next is not None:
            self.current = self.current.next
        ret = self.current.item
        prev = self.current.prev
        del self.current
        self.current = prev
        return ret

    def insert_after(self, item, index):
        size = self.size()
        if index < 0 or index >= size:
            raise Exception("Bad index")
        if self.current.next is None:
            right = self.current
            pos = size
            while index != pos:
                self.current = self.current.prev
                pos -= 1
            next_ = self.current.next
            self.current.next = Node(item, self.current, next_)
            if next_ is not None:
                next_.prev = self.current.next
            self.current = right
            while self.current.next is not None:
                self.current = self.current.next
            return
        if self.current.prev is None:
            left = self.current
            pos = 0
            while index != pos:
                self.current = self.current.next
                pos += 1
            next_ = self.current.next
            self.current.next = Node(item, self.current, next_)
            if next_ is not None:
                next_.prev = self.current.next
            self.current = left
            while self.current.prev is not None:
                self.current = self.current.prev
            return

    def insert_before(self, item, index):
        size = self.size()
        if index < 0 or index >= size:
            raise Exception("Bad index")
        if self.current.next is None:
            right = self.current
            pos = size - 1
            while index != pos:
                self.current = self.current.prev
                pos -= 1
            prev = self.current.prev
            self.current.prev = Node(item, prev, self.current)
            if prev is not None:
                prev.next = self.current.prev
            self.current = right
            while self.current.next is not None:
                self.current = self.current.next
            return
        if self.current.prev is None:
            left = self.current
            pos = 0
            while index != pos:
                self.current = self.current.next
                pos += 1
            prev = self.current.prev
            self.current.prev = Node(item, prev, self.current)
            if prev is not None:
                prev.next = self.current.prev
            self.current = left
            while self.current.prev is not None:
                self.current = self.current.prev
            return

    def delete_index(self, index):
        size = self.size()
        if size == 0:
            raise Exception("List was empty")
        if index < 0 or index >= size:
            raise Exception("Bad index")
        if self.current.next is None:
            right = self.current
            pos = size
            while index != pos:
                self.current = self.current.prev
                pos -= 1
            prev = self.current.prev
            next_ = self.current.next
            ret = self.current.item
            prev.next = next_
            next_.prev = prev
            del self.current
            self.current = right
            return ret
        if self.current.prev is None:
            left = self.current
            pos = 0
            while index != pos:
                self.current = self.current.next
                pos += 1
            prev = self.current.prev
            next_ = self.current.next
            ret = self.current.item
            prev.next = next_
            next_.prev = prev
            del self.current
            self.current = left
            return ret

    def __str__(self):
        if self.is_empty():
            return "[]"
        ret = "["
        if self.current.next is None:
            while self.current.prev is not None:
                self.current = self.current.prev
        if self.current.prev is None:
            while self.current.next is not None:
                ret += str(self.current.item) + ", "
                self.current = self.current.next
        ret += str(self.current.item) + "]"
        return ret


dlist = DoubleList()

dlist.add_end(1)
dlist.add_end(2)
dlist.add_start(3)

print(str(dlist))

dlist.delete_index(1)

print(str(dlist))

dlist.insert_before(5, 0)
dlist.insert_after(6, 1)

print(str(dlist))

dlist.delete_index(2)

print(str(dlist))
