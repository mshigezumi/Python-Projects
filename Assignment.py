var1 = "this is a string"
print(var1)
var2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(var2)
print(var2[2:5])
len(var2)
var3 = " this is a test "
print(var3.strip())
print(var2.upper())
if "Lorem" in var2:
    print("yes")

if "Lorem" not in var2:
    print("yes")

print(var1 + var2)
var4 = "this is a \"test\""
print(var4)

animal = ("zebra", "alligator", "giraffe", "goat", "ox")
listofAnimals = list(animal)
print(listofAnimals)
listofAnimals.append("honey badger")
print(listofAnimals)

myString = "Hello! I am pleased to meet you"
newString = myString.split(" ")
print(newString)

myDictionary = {'index1':1,'index2':2,'index3':355}
print(myDictionary.get('index3'))
myDictionary.update({'index2':200})
myDictionary['index4'] = 4000
myNestedDictionary = {'item1':{"color":'blue',"amount":20},'item2':{"color":'red',"amount":10}}
x = ('key1','key2','key3')
y = 0
thisDict = dict.fromkeys(x,y)
print(thisDict)

myArray = [1,2,3,4,5]

a = 1
b = 2
if a > b:
    print(True)
else:
    print(False)

i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1

name = 'Python'
print(len(name))

for i in enumerate(name):
    print(i)

x = lambda a, b: a + b
print(x(5,10))

def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

getSum(2,4)
myAdd = getSum
myAdd(2,4)
