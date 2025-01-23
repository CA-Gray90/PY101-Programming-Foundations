# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# Will output "hello there", since str2 was originally referencing the same object
# as str1, i.e. "hello there". On line 5 however we reassign str2 to a new variable
# str1 still references the original object "hello there"