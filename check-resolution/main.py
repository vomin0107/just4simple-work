from PIL import Image
import os
import glob

# 이미지가 있는 폴더 경로
path = r'C:\Users\hong0\PycharmProjects\image-scrapping\images'

# glob, os 비교
glob_files = glob.glob(path + "\*.jpg")
os_files = os.listdir(path)
ToT320 = []
ToT224 = []

# print(glob_files)
# print(os_files)

# 해상도 조절 후 저장
for image in glob_files:
    image_file = Image.open(image)
    if image_file.size[1]<320 or image_file.size[0]<320:
        print(image, end=' ')
        print(image_file.size)
        ToT320.append(image)
    if image_file.size[1]<224 or image_file.size[0]<224:
        print(image, end=' ')
        print(image_file.size)
        ToT224.append(image)

print(len(ToT320))
print(len(ToT224))

print('Done.')