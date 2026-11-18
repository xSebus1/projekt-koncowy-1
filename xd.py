from pathlib import *

path = Path("openAi.txt")

sum = 0
allnum = 0


if path.is_file():
    with open(path, "r", encoding="utf-8") as file:
        for num_line, line in enumerate(file, start=1):
            text = line.strip()


            try:
                num = int(text)
                allnum += 1
                sum + text
            except ValueError:
                break
        print(f" Suma wszystkich liczb to {sum}")
        with open("save.txt", "a", encoding="utf-8") as file_save:
            file_save.write(f"Suma wszystkich liczb to {sum}")

else:
    print("Brak pliku")
