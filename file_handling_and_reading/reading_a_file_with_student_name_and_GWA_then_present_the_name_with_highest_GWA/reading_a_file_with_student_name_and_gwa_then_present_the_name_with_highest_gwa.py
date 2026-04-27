class HighestGwa:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def file_read(self) -> list[str]:
        with open(self.filename, "r") as file:
            content = [line.rstrip("\n") for line in file.readlines()]
        return content