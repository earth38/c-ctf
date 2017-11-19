#coding:utf-8
from PIL import Image

with open("picture") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


for (i,x) in enumerate(lines):
    #画像の読み込み
    im = Image.open(x) 
    #im = Image.open(line)
    #RGBに変換
    rgb_im = im.convert('RGB')
    #画像サイズを取得
    size = rgb_im.size
    #取得したサイズと同じ空のイメージを新規に作成
    if i == 0:
        im2 = Image.new('RGBA',size)
    #loop
    for x in range(size[0]):
        #y
        for y in range(size[1]):
            #ピクセルを取得
            r,g,b = rgb_im.getpixel((x,y))
           #set pixel
            if i == 0:
                im2.putpixel((x,y),(r,g,b,0))
            elif g != 0:
                im2.putpixel((x,y),(r,g,b,0))
            else:  
                pass
#show
im2.show()
