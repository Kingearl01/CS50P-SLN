class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🥧" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    # @capacity.setter
    # def capacity(self, value):
    #     try:
    #         if int(value) < 0:
    #             raise ValueError()
    #     except ValueError:
    #        raise ValueError()
    #     self._capacity = value


    

    # @size.setter
    # def size(self, value):
    #     self._size += value




def main():
    jar = Jar()
    jar.deposit(10)
    print(jar.capacity)
    print(jar.size)
    # print(jar.size)


if __name__ == "__main__":
    main()
























#     class Jar:
#     def __init__(self, capacity=12):
#         if capacity < 0:
#             raise ValueError
#         self.capacity = capacity
#         self.size = 0

#     def __str__(self):
#         return "🍪" * self.size

#     def deposit(self, n):
#         if n > self.capacity or n + self.size > self.capacity:
#             raise ValueError
#         self.size += n

#     def withdraw(self, n):
#         if n > self.size:
#             raise ValueError
#         self.size -= n
#     # @property
#     # def capacity(self):

#     # @property
#     # def size(self):

# def main():
#     jar = Jar(4)
#     jar.deposit(2)
#     print(jar)



# if __name__ == "__main__":
#     main()