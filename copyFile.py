from pathlib import Path
import shutil
from tqdm import tqdm

path = Path("C:\\Users\\DIS\\Desktop\\estimation\\test2")
output = Path("C:\\Users\\DIS\\Desktop\\estimation\\test")
#output = Path("/media/smartcoop/PortableSSD")
image_list = list(path.glob("**/*.jpg"))
        
with tqdm(total=len(image_list), desc="filecopyfile") as p:
    for i in image_list:
        shutil.copy2(i, output)
        p.update()