#author: DMH 12/1/21

def total_sum(x):
    total = 0
    for i in range(x + 1):
        total += i
    return total

number = input("What is your number?")

sum = total_sum(int(number))
print(sum)    