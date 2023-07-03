import os
from glob import glob
import shutil
from tqdm import tqdm

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error'+directory)

path_img = glob('C:\\Users\\DIS\\Desktop\\estimation\\test2\\*.jpg')
path_img_op = 'C:\\Users\\DIS\\Desktop\\estimation\\test'

with tqdm(total=len(path_img), desc="file move") as p:
    for i in path_img:
        name = i.split('/')[-1]
        path = name.split('_')
        ppath = os.path.join(path_img_op,path[1],path[2],path[3])
        createFolder(ppath)
        #shutil.copy(i,ppath)
        shutil.move(i,ppath)
        p.update()