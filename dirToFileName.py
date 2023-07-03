from pathlib import Path
from tqdm import tqdm

path = Path("W:\\Data_5-3_back\\001_newCollect\\재업로드")

if __name__ == '__main__':
    countObj = {}
    
    files = list(path.glob('**/*.jpg'))
    
    with tqdm(total=len(files)) as pbar:
        for file in files:
            target = '_'.join([file.parent.parts[-2], file.parent.parts[-1]])
            
            if target in countObj:
                countObj[target] = countObj[target] + 1
            else:
                countObj[target] = 1
            
            newName = f"{target}000{countObj[target]}.jpg"
            
            file.rename(file.parent.parent / newName)
            pbar.update()