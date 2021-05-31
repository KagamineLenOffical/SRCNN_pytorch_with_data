from PIL import Image
import os
src='Data/'  #源文件夹
dst='CropData/'#目的文件夹
size=32#单张图片大小(32*32)
cnt=0
imgs=os.listdir(src)
for opath in imgs:
    path=src+opath
    print(path)
    img=Image.open(path)
    sz=img.size
    print(sz)

    for i in range(sz[0]//size):
        for j in range(sz[1]//size):
            crop_box=(i*size,j*size,(i+1)*size,(j+1)*size)
            #print(crop_box)
            crop_im=img.crop(crop_box)
            #print(crop_im)
            #crop_im.show()
            crop_im.save(dst+'{}.bmp'.format(cnt))
            cnt=cnt+1