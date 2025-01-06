"""1. Write a program to print numbers from 1 to 10 using a for loop."""
for num in range(1, 11): # range(1, 11) generates numbers from 1 to 10
    print(num, end=' ') # print the number followed by a space
    
    
"""2. Take a string (e.g., "Python") and print each character individually using a for loop."""
text = input("Enter a text: ") # a string
print("The characters of the string are:")
for char in text: # iterate over the characters of the string
    print(char, end="  ") # print the character followed by a space
    
    
"""3. Use the range() function to find the sum of numbers from 5 to 15."""
sum = 0 # initialize sum to 0
for num in range(5,16): # range(5, 16) generates numbers from 5 to 15
    sum += num # add num to sum
print("Sum of numbers from 5 to 15 is", sum) # print the sum


"""4. Given a list (e.g., [2, 4, 6, 8, 10]), multiply each item by 2 and print the result."""
myList = [2, 4, 6, 8, 10] # the given list
for num in myList: # iterate through the list
    mul = num*2 # multiplying the number in the list(myList) with 2
    print(f"{num} * 2 = {mul}") # print the result
    
    
"""5. Write a program to print numbers between 1 and 50 that are divisible by 5."""
print("Numbers divisible by 5 between 1 to 50 are:")
for num in range (1, 51): # range(1, 51) generates numbers from 1 to 50
    if num % 5 == 0: # check if num is divisible by 5
        print(num, end=' ') # print the number followed by a space