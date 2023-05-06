class HashMap:
    def __init__(self):
        self.total_size = 7
        self.key_lyst = []
        self.value_lyst = [None] * self.total_size

    def calculation(self, key):
        """returns the index for the values of key in the hashmap
        """

        if isinstance(key[0], tuple):
            result = ((key[0][0] + key[0][1]) + key[-1]) % self.total_size
        else:
            result = ((key[0] + key[1]) % self.total_size)
        return result

    def get(self, key):
        """returns the value for key if key is in the hashmap
        """

        for k in range(len(self.key_lyst)):
            if key == self.key_lyst[k][0] or key == self.key_lyst[k]:
                # calculate index of value_lyst and return value at index
                return self.value_lyst[self.key_lyst[k][-1]]
        raise KeyError("Key is not in HashMap")

    def set(self, key, value):
        """adds the (key, value) pair to the hashmap
        """

        for k in range(len(self.key_lyst)):
            if key == self.key_lyst[k][0] or key == self.key_lyst[k]:
                self.value_lyst[self.key_lyst[k][-1]] = value
                break
        i = self.calculation(key)
        while self.value_lyst[i] is not None:
            i = self.calculation((key, i))

        self.key_lyst.append((key, i))
        self.value_lyst[i] = value

        if len(self.key_lyst) / self.total_size >= 0.8:
            temp_keys = self.key_lyst
            temp_values = self.value_lyst
            self.total_size = (self.total_size * 2) - 1
            self.key_lyst = []
            self.value_lyst = [None] * self.total_size
            for k in temp_keys:
                self.set(k[0], temp_values[k[-1]])

    def remove(self, key):
        """removes the key and its associated value from the map
        """

        for k in range(len(self.key_lyst)):
            if key == self.key_lyst[k][0] or key == self.key_lyst[k]:
                # calculate index of value_lyst and return value at index
                self.value_lyst[self.key_lyst[k][-1]] = None
                self.key_lyst.remove(self.key_lyst[k])
                break

    def clear(self):
        """empties the hashmap of all key-values"""

        self.total_size = 7
        self.key_lyst = []
        self.value_lyst = [None] * self.total_size

    def capacity(self):
        """returns the current capacity--number of buckets--in the map"""

        return self.total_size

    def size(self):
        """returns the number of key-value pairs in the map"""

        return len(self.key_lyst)

    def keys(self):
        """returns a list of keys"""

        temp = []
        for i in self.key_lyst:
            temp.append(i[0])
        return temp

    def __str__(self):
        """returns a string list of key-value pairs"""

        temp = []
        for i in self.key_lyst:
            temp.append((i, self.get(i)))
        return str(temp)
