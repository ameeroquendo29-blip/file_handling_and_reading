class EvenOddSeparator:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename = filename

    def file_read(self) -> list[int]:
        try:
            with open(self.filename, r) as file:
                numbers = [int(number.rstrip("\n")) for number in file.readlines()
            return numbers

        except FileNotFoundError:
            print(f"File {self.filename} doesn't exist")
        except:
            print("Make sure the file only contains integers")

    def file_write(self, filename: str, content: int):
        with open(filename, "a") as file:
            file.write(f"{content}\n")

    def categorize(self):
        data = self.file_read()
        for number in data:
            if number % 2 == 0:
                self.file_write(even.txt, number)
            else:
                self.file_write(odd.txt, number)

if __name__ == "__main__":
    separator = EvenOddSeparator()
    separator.categorize()

