def summer_69(arr):
    six_index = arr.index(6)
    nine_index = arr.index(9)
    sum = 0
    for i in arr:
        if six_index<=arr.index(i) and arr.index(i)<=nine_index:
            continue
        else:
            sum+=i
    return sum
print(summer_69([1,2,3,6,7,8,9,1]))
print(summer_69([1,5,6,9,1,2]))