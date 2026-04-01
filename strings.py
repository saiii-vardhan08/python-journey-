#basic string operations in python
#these methods wont change the original string it will create a new string 
course = 'python for beginners'

print(course.upper())
print(course)

name = "sai is famous name"

print(name.upper())
print(name.lower())
print(name.find('a'))# if this is present in string then it will return index
print(name.find('l')) # if there is nothing like this in string then it will return -1;

#if we want to replace something over something in string then we go for replace method
print(name.replace('is','!$'))

# we can check weather the string is contain in original string or not by using in method
print('sai' in name)# returns boolean valur means true or false