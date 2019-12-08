import matplotlib.pyplot as bla
# function given
def f(n):
    if n <= 9:
        return n*n - 7
    return f(n - 10)

if __name__ == '__main__':
    # loop
    a = []
    b = []
    for i in range(1, 100):
        a.append(i)
        b.append(f(i))

    print(a)
    print(b)
    # plotting
    bla.stem(a, b)
    # label x and y axis
    bla.xlabel('X Axis')
    bla.ylabel('Y Axis')
    # graph title
    bla.title('Graph of f(n)')
    # to see graph in concole
    bla.show()