def show_highest_gwa(data: list):
    if not data:
        print("No data to process.")
        return
    try:
        new_data = [info.split(",") for info in data]
        highest_gwa = max(new_data, key=lambda x: float(x[1]))
        print(f"Highest GWA (Best Grade)")
        print(f"Student: {highest_gwa[0]}")
        print(f"GWA: {highest_gwa[1]}")
    except ValueError:
        print("Error: A GWA value in your file is not a valid number.")


class HighestGwa:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def file_read(self) -> list[str]:
        with open(self.filename, "r") as file:
            content = [line.strip("\n") for line in file.readlines()]
        return content


if __name__ == "__main__":
    gwa = HighestGwa()
    data = gwa.file_read()
    show_highest_gwa(data)