from PIL import Image

i = 0
for num1 in range(64):
#print("num1 = " + str(num1))
    im1 = Image.new("RGB",(10,450),(0,0,0))
    
    for num2 in range(45):
    #print(" num2 = " + str(num2))
        im2 = Image.open("bunkai/anime" + str(i) + ".gif")
        im1.paste(im2,(0,(num2)*10))
        i+=1
    im1.save('renketsu/renketsu' + str(num1) + '.gif')

im3 = Image.new ("RGB",(640,450))
for num3 in range(64):
    im4 = Image.open('renketsu/renketsu' + str(num3) + '.gif')
    im3.paste(im4,(num3*10,0))
im3.save("renketsu/ok.gif")
