# Run after initial list creation from 01-CardNumberGenerator-LuhnCheck.py
# Create basic list of viable test credit card numbers.

def extract_number(line):
    # Extract the number from the line
    number = line.split()[0]
    return number

def main():
    input_filename = "numbers.txt"
    output_filename = "viablenumbers.txt"

    viable_numbers = []

    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            if "Passed Luhn algorithm check" in line:
                number = extract_number(line)
                viable_numbers.append(number)

    with open(output_filename, "w") as output_file:
        for number in viable_numbers:
            output_file.write(number + "\n")

if __name__ == "__main__":
    main()
