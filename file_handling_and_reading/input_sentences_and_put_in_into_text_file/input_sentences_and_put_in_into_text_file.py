class InputMultipleLines:
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename

    def input_lines(self):
        try:
            with open(self.filename, "a") as file:
                while True:
                    line = input("Enter a line: ")
                    more_lines = input("Are there any more lines (y/n)? ").lower()
                    file.write(f"{text}\n")
                    if more_lines != "y":
                        break
        except FileNotFoundError:
            print("File not found.")
        except:
            print("Error in writing the file.")
