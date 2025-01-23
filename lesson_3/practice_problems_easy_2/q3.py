# Programmatically determine whether 42 lies between 10 and 100, inclusive.
# Do the same for the values 100 and 101.

def is_between_10_100(number):
    print(number in range(10, 101))

is_between_10_100(42)
is_between_10_100(100)
is_between_10_100(101)