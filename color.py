from colorthief import ColorThief
import colorsys
import time
import numpy
import Image

while True:
    #img = cv2.imread('/var/lib/motion/Photo.jpg')
    #roi = img[240:480, 240:400]
    #cv2.imshow("cropped", roi)
    #cv2.waitKey(1)
    #roi_array = Image.fromarray(roi)
    #roi_array.save('Photo.jpg')
    img = Image.open('/var/lib/motion/Photo.jpg')
    #w, h = img.size
    cropped = img.crop((240,240,400,480))
    cropped.save("Photo.jpg")
    color_thief = ColorThief("Photo.jpg")
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    r = float(dominant_color[0])
    g = float(dominant_color[1])
    b = float(dominant_color[2])
    print r,g,b
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    print h
    print s
    print v
    s = s*2
    v = v*1.5

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    print r,g,b
    # build a color palette
    palette = color_thief.get_palette(color_count=6)
    print palette[1]
    secondary = palette[1]
    r2 = float(secondary[0])
    g2 = float(secondary[1])
    b2 = float(secondary[2])
    print r,g,b
    h2, s2, v2 = colorsys.rgb_to_hsv(r2, g2, b2)
    print h2
    print s2
    print v2
    s2 = s2*5
    v2 = v2*1.5

    r2, g2, b2 = colorsys.hsv_to_rgb(h2, s2, v2)

    # with is like your try .. finally block in this case
    with open('myStyles.css', 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    # now change the 8th line, note that you have to add a newline
    majority = "47.5%"
    data[8] = 'rgb(%d,%d,%d) %s\n' % (r,g,b,majority)

    # now change the 7th line, note that you have to add a newline
    minority = "52.5%"
    data[7] = 'rgb(%d,%d,%d) %s,\n' % (r2,g2,b2,minority)

    # and write everything back
    with open('MyStyles.css', 'w') as file:
        file.writelines( data )
    time.sleep(2)
