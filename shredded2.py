import numpy as np
from PIL import Image

order = [0, 9, 11, 5, 6, 25, 2, 16, 15, 26,3, 20, 19, 21, 10, 23, 7, 8, 1, 24, 22, 4, 18, 14, 12, 13 ,17]
imgfiles = ["./{}.png".format(i) for i in order]
images = map(Image.open, imgfiles)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

new_im.save('test_ordered.jpg')
