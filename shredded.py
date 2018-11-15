import numpy as np
from PIL import Image

imgfiles = ["./{}.png".format(i) for i in range(27)]
images = map(Image.open, imgfiles)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

new_im.save('test.jpg')
