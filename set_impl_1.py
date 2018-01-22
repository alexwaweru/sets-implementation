class Superset():
    def __init__(self):
        self.slots = []

    '''Adds an element into the set'''
    def add(self, element):
        element = str(element)
        self.slots.append(element)

    def __str__(self):
        if len(self.slots) > 0:
            string = '{' + str(self.slots[0])
            newlist = self.slots[1:]
            for i in range(len(newlist)):
                string = string + ', ' + str(newlist[i])
            string = string + '}'
        else:
            string = ''
            
        return string

class Set():
    def __init__(self, Superset):
        self.size = len(Superset.slots)
        self.superset = Superset
        self.slots = [0]*self.size

    '''Adds an element into the set'''
    def add(self, element):
        element = str(element)
        for i in range(len(self.superset.slots)):
            if self.superset.slots[i]==element:
                self.slots[i]=1

    def convert_from_binary(self, setA):
        output = []
        for i in range(len(self.superset.slots)):
            if setA[i]==1:
                output.append(self.superset.slots[i])
        return output

    '''Combines the elements in two sets into 1'''
    def union(self, setB):
        union = Set(self.superset)
        union.slots = [0]*self.size
        for i in range(len(setB.slots)):
            if setB.slots[i]==1 or self.slots[i]==1:
                union.slots[i]=1
        union.slots=self.convert_from_binary(union.slots)
        return union

    '''Returns the elements that are both common in two sets'''
    def intersection(self, setB):
        inter = Set(self.superset)
        inter.slots = [0]*self.size
        for i in range(len(setB.slots)):
            if setB.slots[i]==1 and self.slots[i]==1:
                inter.slots[i]=1
        inter.slots = self.convert_from_binary(inter.slots)
        return inter

    '''Returns the elements in set A that are not present in set B'''
    def difference(self, setB):
        diff = Set(self.superset)
        diff.slots = [0]*self.size
        for i in range(len(setB.slots)):
            if self.slots[i]==1 and setB.slots[i]==0:
                diff.slots[i]=1
        diff.slots = self.convert_from_binary(diff.slots)
        return diff

    '''Returns the elements in the superset that are not in the set'''
    def compliment(self):
        comp = Set(self.superset)
        comp.slots = [0]*self.size
        for i in range(len(self.superset.slots)):
            if (self.slots[i]==0):
                comp.slots[i] = 1
        comp.slots = self.convert_from_binary(comp.slots)
        return comp

    '''Overides the default add function'''
    def __add__(self, setB):
        return self.union(setB)

    '''Overides the default subtraction function'''
    def __sub__(self, setB):
        return self.difference(setB)

    '''Overides the [] parameter'''
    def __getitem__(self, element):
        return self.find(element)

    '''Creates the string representation of the object for the print function'''
    def __str__(self):
        if len(self.slots) > 0:
            string = '{' + str(self.slots[0])
            newlist = self.slots[1:]
            for i in range(len(newlist)):
                string = string + ', ' + str(newlist[i])
            string = string + '}'
        else:
            string = '{}'
        return string

#Create superset
U = Superset()

#Populate superset
U.add(1); U.add(2); U.add(3); U.add(4); U.add(5); U.add(6); U.add(7); U.add(8); U.add(9); U.add(10)

#Create subsets
A = Set(U); B = Set(U); C = Set(U); D = Set(U)

#Populate subsets
A.add(1); A.add(7); A.add(2); A.add(3); A.add(9)
B.add(3); B.add(5); B.add(2); B.add(4)
C.add(1); C.add(2); C.add(3); C.add(4); C.add(5)
D.add(5); D.add(2); D.add(8); D.add(10)

Union = A + B #Union
Difference = A - B #Difference
Intersection = A.intersection(B) #Intersection
Compliment = B.compliment() #Compliment

B.slots = B.convert_from_binary(B.slots); C.slots = C.convert_from_binary(C.slots)
D.slots = D.convert_from_binary(D.slots); A.slots = A.convert_from_binary(A.slots)

print('superset U \n', U, '\n'); print('subset A \n', A, '\n'); print('subset B \n', B, '\n'); print('subset C \n', C, '\n'); print('subset D \n', D, '\n')
print('Union of subsets A and B\n',Union, '\n'); print('Difference of subsets A and B\n', Difference, '\n'); print('Intersection of subsets A and B\n', Intersection, '\n')
print('Complimet of subset B\n', Compliment, '\n')
