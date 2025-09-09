

import os
from pathlib import Path

root_dir = Path("TEST")

for root, dirs, files in os.walk(root_dir, followlinks=False):
    for name in files:
        file_path = Path(root) / name
        
        try:
            with file_path.open("r", encoding="utf-8", errors="replace") as f:
                content = f.read()
                print(content)
            
            with file_path.open("a", encoding="utf-8", errors="replace") as f:
                f.write("\nNAME = RAGHU")
                print(f"Replaced content in {file_path}")

        except Exception as e:
          print(f"Skipping {file_path}: {e}")
                       
       


