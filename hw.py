def count_odds(lst):
    num_odds = 0
    for num in lst:
        if num % 2 != 0:
            num_odds += 1
    return(num_odds)
result = count_odds([1, 2, 3, 4])
print(result)