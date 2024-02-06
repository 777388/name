import sys
import math
class consider:
    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    
    def nondeterminism(self):
        print("nondeterminism:")
        numbers = []
        v=[]
        t = [self.name1, self.name2, self.name3]
        for i in range(len(t)):
            d = 0
            for j in range(len(t[i])):
                d += ord(t[i][j])
            if d in numbers:
                continue
            else:
                numbers.append(d)
            v.append(d)
        for k in range(len(t)):
            for e in range(len(t[k])):
                for p in range(math.ceil(v[k])):
                    b = ord(t[k][e])-ord(t[k][e])/v[k]
                    if b in numbers:
                        continue
                    else:
                        numbers.append(b)
        for g in numbers:
            print(g)
            print(chr(math.ceil(g)))

    def pi(self):
        print("pi")
        numbers = []
        v = []
        t = [self.name1, self.name2, self.name3]
        for i in range(len(t)):
            d = float(0)
            for j in range(len(t[i])):
                d += float(ord(t[i][j]))-float(ord(t[i][j]))/ float(ord(t[i][j])*2.314)
            if d in numbers:
                continue
            else:
                numbers.append(d)
            v.append(d)
        for k in range(len(t)):
            for e in range(len(t[k])):
                for p in range(math.ceil(v[k])):
                    b = float(ord(t[k][e]))-float(ord(t[k][e]))/ float(v[k] * 2.314)
                    if b in numbers:
                        continue
                    else:
                        numbers.append(b)
        for g in numbers:
            print(g)
            print(chr(math.ceil(g)))

    def inform(self):
        print("inform")
        t = [self.name1, self.name2, self.name3]
        for i in range(len(t)):
            l = 0
            v = 0
            print(i, t[i])
            for j in range(len(t[i])):
                print(t[i][j], str(ord(t[i][j])), str(int(ord(t[i][j]))-int(ord(t[i][j]))/int(ord(t[i][j]) * 2.314)))
                v += ord(t[i][j])
                l += int(ord(t[i][j]))-int(ord(t[i][j]))/int(ord(t[i][j]) * 2.314)
                print("added up ", str(v), str(l))
                print(chr(math.ceil((v))), chr(math.ceil((l))))

class reconsider(consider):
    def __init__(self, name1, name2, name3):
        super(reconsider, self).__init__(name1, name2, name3)
distribute = reconsider(sys.argv[1], sys.argv[2], sys.argv[3])

distribute.pi()
distribute.nondeterminism()
distribute.inform()
