# Write a function is_even that will return true if the passed-in number is even.

y = 5
x = 2

def is_even(x):
    return x % 2 == 0
        
print(is_even(x))
print(is_even(y))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Print out "Even!" if the number is even. Otherwise print "Odd"
