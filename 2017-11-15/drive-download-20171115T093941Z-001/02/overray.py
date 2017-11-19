#coding:utf-8
from PIL import Image

def getFilenames(directory):
    with open(directory) as f:
        filenames = f.readlines()
        filenames = [filename.strip() for filename in filenames]
        return filenames

def overrayImages(filenames):
    row,column = getSize(filenames[0])
    #取得したサイズと同じ空のイメージを新規に作成
    im2 = Image.new('RGBA',(row,column))
    for filename in filenames:
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        #行
        for x in range(row):
            #列
            for y in range(column):
                #ピクセルを取得
                r,g,b = rgb_im.getpixel((x,y))
                setPixel(im2,x,y,r,g,b)
        
    return im2


def setPixel(im,x,y,r,g,b):
    if g != 0:
        im.putpixel((x,y),(r,g,b,0))

    return im
    
def getSize(filename):
    #画像の読み込み
    im = Image.open(filenames[0])
    #RGBに変換
    rgb_im = im.convert('RGB')
    #画像サイズを取得
    size = rgb_im.size
    row,column = size[0],size[1]
    return row,column


if __name__ == "__main__":
    filenames = getFilenames("images")
    im2 = overrayImages(filenames)
    im2.show()
