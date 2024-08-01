from pathlib import Path
import shutil
from tqdm import tqdm

path = Path("<input file path>")
output = Path("<output file path>")
image_list = list(path.glob("**/*.jpg"))
        
with tqdm(total=len(image_list), desc="filecopyfile") as p:
    for i in image_list:
        shutil.copy2(i, output)
        p.update()
