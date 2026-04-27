class InputMultipleLines:
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename

    def input_lines(self):
        try:
            with open(self.filename, "a") as file:
                while True:
                    sentence = input("Enter a line: ")
                    more_lines = input("Are there any more lines (y/n)? ").lower()
                    file.write(f"{sentence}\n")
                    if more_lines != "y":
                        break
        except FileNotFoundError:
            print("File not found.")

if __name__ == "__main__":
    InputMultipleLines().input_lines()
