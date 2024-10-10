def generate_fibonacci(n):
    t1, t2 = 0, 1
    print("\nFibonacci Sequence up to", n, "terms:")
    print(t1, t2, end=", ")

    for i in range(3, n + 1):
        next_term = t1 + t2
        print(next_term, end=", " if i < n else "\n")
        t1, t2 = t2, next_term

def main():
    print("====================================")
    print("     Fibonacci Sequence Generator   ")
    print("====================================")

    try:
        n = int(input("Enter the number of terms you want to generate: "))

        if n <= 0:
            print("\nPlease enter a positive integer.\n")
        else:
            generate_fibonacci(n)

    except ValueError:
        print("\nInvalid input! Please enter an integer.\n")

    print("====================================")
    print("           Program Ended            ")
    print("====================================")

if __name__ == "__main__":
    main()
