from doubly_linked_list import DoublyLinkedList
import _collections


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.cache = _collections.OrderedDict()

    def append(self, item):
        try:
            # pop the item off
            value = self.cache.pop(item)
            # set value to the front
            #  1,2,3,4 will become 4,1,2,3
            self.cache[item] = value
            return value
        # KeyError happens when item is not in dictionary
        except KeyError:
            return None

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents.append(self.cache)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
