class EvenOddSeparator:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename = filename

    def file_read(self) -> list[int]:
        try:
            with open(self.filename, r) as file:
                numbers = [int(number.rstrip("\n")) for number in file.readlines()
            return numbers

    def file_write(self, filename: str, content: int):
        with open(filename, "a") as file:
            file.write(f"{content}\n")

