def blackjack(a,b,c):
    x = sum((a,b,c))
    if x <= 21:
        return x
    elif x > 21 and 11 in (a,b,c):
            return x-10
    elif x > 21:
        return 'BUST'
print(blackjack(9,9,9))
print(blackjack(5,6,11))
print(blackjack(5,6,7))

