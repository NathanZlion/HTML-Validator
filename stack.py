# SECTION: 1
# Dawit Zeleke          UGR/7912/13
# Nathnael Dereje       UGR/8587/13
# Zekariyas Teshager     UGR/5840/13



class Stack:
   
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list)-1]

    def size(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)
