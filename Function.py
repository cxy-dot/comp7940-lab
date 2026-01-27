# Write a function that prints all factors of the given parameter x
def print_factor(x):
    for i in range(2, x):
        if x % i == 0:
            print(i)

l = [52633, 8137, 1024, 999]

for x in l:
    print(f"Factors of {x}:")
    print_factor(x)
    print()
