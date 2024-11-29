# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


x = 1
y = 35656222554887711
z = -32555141522

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(type(x) , type(y) , type(z))


a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = "Hello \bWorld!"
print(txt)


txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

txt = "python is FUN!"

x = txt.capitalize()

print (x)

txt = "banana"

x = txt.center(20)

print(x)

txt = "banana"

txt = txt.center(20, "a")

print(txt)

print(txt.count("a"))


print(10 > 9)
print(10 == 9)
print(10 < 9)


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


x = 200
print(isinstance(x, int))


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry", "apple", "cherry"]


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:6] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
