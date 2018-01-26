def tally():
    score = 0
    while True:
        increment = yield score
        score += increment


white = tally()
blue = tally()
print(next(white))
print(next(blue))
print(white.send(1))
print(white.send(2))
print(white.send(3))
print(blue.send(4))
print(blue.send(5))
print(next(blue))
