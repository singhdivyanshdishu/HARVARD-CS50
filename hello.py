"""
name =input("What is ur name?")

print("Hello, My name is " + name )

print ("Oh! Hi, ")
print(name )
"""

name =input("What is ur name?")

print("Hello, My name is " + name )


#concatenation
print ("Oh! Hi, "+ name)

#print(*objects, sep=' ', end='\n', file=None, flush=False)
#passing two arguments
print ("Oh! Hi, ", name)

print(f"Hello {name}")

print("Hi ," )
print(name)


print("Hi ," , end = "")
print(name)


# print("Hi "friend"")
print('Hi "friend"')
print("Hi \"friend\"")



#remove white space
name = name.strip()
name =name.capitalize() #first letter capital
print(f"Hello {name}")
name =name.title() #first letter of each word capital
print(f"Hello {name}")


name = input("enter the name again ").strip().title()
print(name )


#split user name firstname and second name
first , last = name.split(" ")
print(f"Hello {first}")
