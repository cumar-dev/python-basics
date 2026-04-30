# File handling

import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "text.txt")

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())


with open("cade.txt", "w", encoding="utf-8") as file:
    file.write("Hello omar")
    file.write("\n what do you want to do today?")    

with open("cade.txt", "r", encoding="utf-8") as file:
    print(file.read());

with open("text.txt", "r", encoding="utf-8") as f:
    print(f.read());

with open("cade.txt", "a", encoding="utf-8") as f:
    f.write("\nToday i am practicing file handling");

with open("omar.txt", "a", encoding="utf-8") as file:
    file.write("\n Today i am practicing file handling");