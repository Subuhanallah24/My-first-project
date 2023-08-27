number = int(input("Enter a number here to know wether it's a even or odd number: "))
x = int(number % 2)
if x == 0:
    print(f"The number {number} is an even number")
else:
    print(f"{number} is an odd number")

