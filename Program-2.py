def generate_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

# Example usage
if __name__ == "__main__":
    a = int(input("Enter a value: "))
    result = generate_series(a)
    print("Output:", ", ".join(map(str, result)))
