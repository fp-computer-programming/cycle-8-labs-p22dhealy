#author: DMH 12/2/21

def sum_to(n):
    total = 0
    x = 0
    while x <= int(n):
        total += x
        x += 1
    return total

value = input("Enter your integer: ")
print(sum_to(value))