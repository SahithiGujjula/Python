def animal_crackers(string):
    x1, x2 = string.split(' ')
    if x1[0].isupper == x2[0].isupper:
        print(True)
    else:
        print(False)
animal_crackers('Crazy Kangaroo')
