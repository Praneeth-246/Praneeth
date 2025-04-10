def count_multiples(numbers):
    result = {}
    for i in range(1, 10):  # From 1 to 9
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

# Example usage
if __name__ == "__main__":
    input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(input_numbers)
    print("Output:")
    print(output)
