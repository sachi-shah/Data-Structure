'''
Deque - Double ended queue

add_first(e): Add element e to the front of deque D.
add_last(e): Add element e to the back of deque D.
delete_first( ): Remove and return the first element from deque D; an error occurs if the deque is empty.
delete_last( ): Remove and return the last element from deque D; an error occurs if the deque is empty.
first(): Return (but do not remove) the first element of deque D; an error occurs if the deque is empty.
last(): Return (but do not remove) the last element of deque D; an error occurs if the deque is empty.
is empty(): Return True if deque D does not contain any elements.
len(D): Return the number of elements in deque D; in Python, we implement this with the special method __len__ .
'''

class Deque:

    
#     initialize
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []
    
    def add_first(self, item):
        self.items.insert(0,item)
    
    def add_last(self, item):
        self.items.append(item)
        
    def delete_first(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items.pop(0)

    def delete_last(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items.pop()

    def __len__(self):
        return len(self.items)
    
    def first(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items[0]
    
    def last(self):
        if self.is_Empty():
            raise Exception('Deque is empty')
        else:
            return self.items[-1]


d=Deque()
print("Is the list empty ? :",d.is_Empty())

d.add_first(2)
print("After add_first(2)  ",d.items)
d.add_first(1)
print("After add_first(1)  ",d.items)

d.add_last(3)
print("After add_last(3)  ",d.items)
d.add_last(4)
print("After add_last(3)  ",d.items)

print("Is the list empty ? :",d.is_Empty())

print(d.delete_first())
print("After delete_first()  ",d.items)

print(d.delete_last())
print("After delete_last()  ",d.items)

print("The length:  ",d.__len__())

print("The first element is  ",d.first())

print("The last element is  ",d.last())
