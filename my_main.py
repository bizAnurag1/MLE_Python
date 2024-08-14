global my_global_variable
my_global_variable = 1000

def add(a,b):
    print(my_global_variable)
    c = a* my_global_variable
    return a+b, c

def sub(a, b):
    return a-b

def main():
    print("my own libraries")
    global my_global_variable
    my_global_variable = 1200
    print(add(20, 10))
    print(sub(40, 10))

if __name__ == '__main__':
    main()

