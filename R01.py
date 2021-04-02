# Birthday problem using Static Array as the data Structure

# implementation of static array

class StaticArray:

    def __init__(self,n):
        self.data = [None] * n

    def get_at(self,i):
        if not(0 <= i < len(self.data)):
            raise IndexError
        return self.data[i]
    
    def set_at(self,i,x):
        if not(0 <= i < len(self.data)):
            raise IndexError
        self.data[i] = x

def birthday_problem(students):
    n = len(students)
    record = StaticArray(n)
    for k in range(n):
        (name1,bday1) = students[k]
        for i in range(k):
            (name2,bday2) = record.get_at(i)
            if bday1 == bday2:
                return (name1,name2)
        record.set_at(k,(name1,bday1))

    return None 


myclass = [("i",7),('s',7),("h",0)]
print(birthday_problem(myclass))