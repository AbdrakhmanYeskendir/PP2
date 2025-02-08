# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)

my_function(3)