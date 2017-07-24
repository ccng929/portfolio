
from PIL import Image



# For recoloring.

darkBlue = (0, 51, 76)

red = (217, 26, 33)

lightBlue = (112, 150, 158)

yellow = (252, 227, 166)



my_image = Image.open("ariana grande.png")

image_list = my_image.getdata()

image_list = list(image_list)




recolored = []

def color(darkBlue,red,lightBlue,yellow,recolored,image_list):
    for pixel in image_list:



        intensity = pixel[0] + pixel[1] + pixel[2]



        if intensity < 182:

            recolored.append(darkBlue)



        elif intensity >= 182 and intensity < 364:

            recolored.append(red)



        elif intensity >= 364 and intensity < 546:

            recolored.append(lightBlue)



        elif intensity >=546:
            recolored.append(yellow)
    return recolored
color(darkBlue,red,lightBlue,yellow,recolored,image_list)



new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
