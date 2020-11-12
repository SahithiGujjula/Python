def has_33(num):
    for x in range(len(num)-1):
        if (num[x] == 3) and (num[x+1] == 3):
            return True
    return False

print(has_33([1, 2, 3, 3]))
print(has_33([3, 3, 1]))
print(has_33([1, 2, 3, 4]))