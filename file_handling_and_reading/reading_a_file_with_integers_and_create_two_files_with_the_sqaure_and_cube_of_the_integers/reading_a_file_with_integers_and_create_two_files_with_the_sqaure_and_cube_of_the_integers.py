class SquareCubeOfTheIntegers:
    def __init__(self, filename: str = "integers.txt"):
        self.filename = filename
        self.square_integers = "double.txt"
        self.cube_integers = "triple.txt"

    def process_numbers(self):
        try:
            with open(self.filename, "r") as file:
                numbers = [int(line.strip()) for line in file if line.strip()]
            with open("double.txt", "w") as double_file, \
                 open("triple.txt", "w") as triple_file:
                for num in numbers:
                    double_file.write(f"{num ** 2}\n")
                    triple_file.write(f"{num ** 3}\n")
            print("Processing complete. Check double.txt and triple.txt.")

