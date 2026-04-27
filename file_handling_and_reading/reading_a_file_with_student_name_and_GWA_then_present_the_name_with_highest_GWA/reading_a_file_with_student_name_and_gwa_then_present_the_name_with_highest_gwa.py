class HighestGwa:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def file_read(self) -> list[str]:
        with open(self.filename, "r") as file:
            content = [line.strip("\n") for line in file.readlines()]
        return content

    def show_highest_gwa(self, data: list):
        new_data = [info.split(",") for info in data]
        highest_gwa = max(new_data, key=lambda x: x[1])
        print(f"Highest GWA\nStudent: {highest_gwa[0]}\nGWA: {highest_gwa[1]}")

if __name__ == "__main__":
    gwa = HighestGwa()
    data = gwa.file_read()
    gwa.show_highest_gwa(data)