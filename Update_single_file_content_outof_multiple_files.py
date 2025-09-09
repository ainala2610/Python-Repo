

import os
from pathlib import Path

user_input = input("Enter the root directory path: ")
root_dir = Path(user_input)
matchtargetfile = list(root_dir.rglob("test1.txt"))
print(matchtargetfile)

if matchtargetfile:
    for match in matchtargetfile:
        print(f"Found: {match}")
        try:
            with match.open("r", encoding="utf-8", errors="replace") as f:
                content = f.read()
                print(content)
            
            with match.open("a", encoding="utf-8", errors="replace") as f:
                f.write("\nNAME = RAJA")
                print(f"Replaced content in {match}")

        except Exception as e:
           print(f"Skipping {match}: {e}")
