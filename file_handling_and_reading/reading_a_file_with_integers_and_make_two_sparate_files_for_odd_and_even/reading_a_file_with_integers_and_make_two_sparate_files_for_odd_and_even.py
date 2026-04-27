class EvenOddSeparator:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename = filename

    def file_read(self) -> list[int]:
        try:
            with open(self.filename, r) as file:
                numbers = [int(number.rstrip("\n")) for number in file.readlines()
            return numbers

