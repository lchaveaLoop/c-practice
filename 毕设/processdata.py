import os
import random
import shutil

a=['agricultural',
'airplane',
'baseballdiamond',
'beach',
'buildings',
'chaparral',
'denseresidential',
'forest',
'freeway',
'golfcourse',
'harbor',
'intersection',
'mediumresidential',
'mobilehomepark',
'overpass',
'parkinglot',
'river',
'runway',
'sparseresidential',
'storagetanks',
'tenniscourt']
i=20

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def getData(src_path):
    dest_dir = 'H:/UCMerced_LandUse/Images/testing/countryside/'  # 这个文件夹需要提前建好
    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list) * 0.8)  # 这个可以修改划分比例
    print(le)
    for f in img_list[le:]:
        print(f)
        shutil.move(f, dest_dir)


# getData('H:/chromDownLoad/UCMerced_LandUse/Images/'+a[i])
getData("H:/chromDownLoad/countryside/")