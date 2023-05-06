def insert(self, value):
    self.heap_array.append(value)
    self.size += 1
    self.heapify_up()
