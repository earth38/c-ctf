#coding:utf-8
from PIL import Image
#画像の読み込み
#im = Image.open("01_white.png")
im = Image.open("01_white.png")
#RGBに変換
rgb_im = im.convert('RGB')
#画像サイズを取得
size = rgb_im.size
#loop
#x
for x in range(size[0]):
    #y
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = rgb_im.getpixel((x,y))https://github.com/earth38/akictf/edit/master/stegoNoobs1.py
        print(str(r) + "," + str(g) + "," + str(b))
