from PIL import Image
#iimport Image
im = Image.open("02_anime2.gif")
while True:
    im.save('bunkai/anime' + str(im.tell()) + '.gif')
    im.seek(im.tell()+1)
