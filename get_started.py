class alma:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("I bought " + name + " apple " + str(weight) + "kg")
    
    def __del__(self):
        print("I ate apple")

def split_apple(a: alma):
    a.weight = a.weight / 2
    return a

buf1 = alma("idared",1)
buf1 = split_apple(buf1)

print(buf1.name)
print(buf1.weight)
print(buf1.__dict__)
print(dir(buf1))
del buf1

buf2 = alma("jonagold",5)
buf2 = split_apple(buf2)

print(buf2.name)
print(buf2.weight)
del buf2