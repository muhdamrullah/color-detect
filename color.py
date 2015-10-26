from colorthief import ColorThief
import colorsys

color_thief = ColorThief('/var/lib/motion/Photo.jpg')
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
s = s*5
v = v*1.5

r, g, b = colorsys.hsv_to_rgb(h, s, v)

print r,g,b
# build a color palette
palette = color_thief.get_palette(color_count=6)
print palette

# with is like your try .. finally block in this case
with open('myStyles.css', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

# now change the 2nd line, note that you have to add a newline
data[3] = '    background: rgb(%d, %d, %d);\n' % (r,g,b)

# and write everything back
with open('MyStyles.css', 'w') as file:
    file.writelines( data )
