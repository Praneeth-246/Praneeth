def generate_custom_series(a: int):
    # If 'a' is even, generate up to 'a - 1' odd numbers
    limit = a if a % 2 != 0 else a - 1
    series = []
    for i in range(limit):
        series.append(2 * i + 1)
    return series

# Main program
if __name__ == "__main__":
    a = int(input("Enter a value: "))
    result = generate_custom_series(a)
    print("Output:", ", ".join(map(str, result)))
