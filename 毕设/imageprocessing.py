import os

from PIL import Image

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
output_dir='H:/UCMerced_LandUse/Images/testing/'+a[i]+'/'
# input_dir='H:/chromDownLoad/UCMerced_LandUse/Images/'+a[i]+'/'

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("new folder:",output_dir.split('/')[-1])

    else:
        print("---this folder is already  ---")

# l=os.listdir(output_dir)

print(output_dir)
mkdir(output_dir)
# s=output_dir.split('/')[-1]
# print(s)

# #read all image from input_dir and save in output_dir
# for i in l:
#     print(input_dir+i)
#     image= Image.open(input_dir+i)
#     image_conv= image.convert('L')
#     image_conv.save(output_dir+i)

#processing files
# source_path='H:/UCMerced_LandUse/Images/'
# dir_train='training/'
# dir_test='testing/'
# files=os.listdir(source_path)
# try:
#     os.mkdir(source_path + dir_train)
#     os.mkdir(source_path + dir_test)
#     for f in files:
#         os.mkdir(source_path+dir_train+f)
#         print(len(source_path+dir_train+f))
#         # print('train_dir:\t',source_path+dir_train+f)
#         os.mkdir(source_path+dir_test+f)
#         # print('test_dir:\t',source_path+dir_test+f)
# except OSError:
#     pass
#
# for f in files:
#     print(len(source_path+dir_train+f))


