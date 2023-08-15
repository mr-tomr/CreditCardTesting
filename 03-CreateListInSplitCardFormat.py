'''
Use after 02-ParseList-SaveViableNumbers.py
Takes a list of numbers made up of 16 digits each and formats them like a credit card.
For example,  1111000011110000 results in 1111 0000 1111 0000
For informational purposes only.
'''

def format_numbers(input_file, output_file):
    with open(input_file, "r") as f:
        numbers = f.readlines()

    formatted_numbers = []

    for number in numbers:
        number = number.strip()

        # Split the number into groups of 4 digits
        groups = [number[i:i+4] for i in range(0, len(number), 4)]

        # Join the groups with spaces, including the last group
        formatted_number = " ".join(groups)

        formatted_numbers.append(formatted_number)

    with open(output_file, "w") as f:
        f.write("\n".join(formatted_numbers))

if __name__ == "__main__":
    input_file = "viablenumbers.txt"  # Replace with your input file path
    output_file = "formatted_numbers.txt"  # Replace with your output file path

    format_numbers(input_file, output_file)

