# Developer : Hamdy Abou El Anein
# fibonacci in Python 3


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()
print([next(fib) for i in range(100)]) #100 = number of sequences.