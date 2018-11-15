from PIL import Image
import copy
from itertools import permutations
from qrtools import QR

order = [0, 9, 11, 5, 6, 25, 2, 16, 15, 26,3, 20, 19, 21, 10, 23, 7, 8, 1, 24, 22, 4, 18, 14, 12, 13 ,17]
imgfiles = ["./{}.png".format(i) for i in order]
images = map(Image.open, imgfiles)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

rightsqborder = [order.index(i) for i in [14, 8]]
leftsqwhites = [order.index(i)  for i in [6, 15]]
rightsqwhites = [order.index(i)  for i in [1, 18]]
leftsmallsq = [order.index(i) for i in [25, 2, 16]]
rightsmallsq = [order.index(i) for i in [24, 22, 4]]
verticalwhites = [order.index(i) for i in [3, 7]]
blackdots = [order.index(i) for i in [20, 21, 23]]
whitedots = [order.index(i) for i in [19, 10]]

images_copy = copy.copy(images)
idx = 0
qr = QR()

for perm1 in permutations(rightsqborder):
    for i in range(len(rightsqborder)):
        images_copy[rightsqborder[i]] = images[perm1[i]]
    
    for perm2 in permutations(leftsqwhites):
        for i in range(len(leftsqwhites)):
            images_copy[leftsqwhites[i]] = images[perm2[i]]
        
        for perm3 in permutations(rightsqwhites):
            for i in range(len(rightsqwhites)):
                images_copy[rightsqwhites[i]] = images[perm3[i]]
            
            for perm4 in permutations(leftsmallsq):
                for i in range(len(leftsmallsq)):
                    images_copy[leftsmallsq[i]] = images[perm4[i]]
                
                for perm5 in permutations(rightsmallsq):
                    for i in range(len(rightsmallsq)):
                        images_copy[rightsmallsq[i]] = images[perm5[i]]
                    
                    for perm6 in permutations(verticalwhites):
                        for i in range(len(verticalwhites)):
                            images_copy[verticalwhites[i]] = images[perm6[i]]
                            
                        for perm7 in permutations(blackdots):
                            for i in range(len(blackdots)):
                                images_copy[blackdots[i]] = images[perm7[i]]
                            
                            for perm8 in permutations(whitedots):
                                for i in range(len(whitedots)):
                                    images_copy[whitedots[i]] = images[perm8[i]]
                                
                                new_im = Image.new('RGB', (total_width, max_height))

                                x_offset = 0
                                for im in images_copy:
                                    new_im.paste(im, (x_offset,0))
                                    x_offset += im.size[0]

                                new_im.save('test_{}.jpg'.format(idx))
                                
                                
                                qr.decode('test_{}.jpg'.format(idx))
                                print(qr.data)
                                
                                if "FLAG" in qr.data:
                                    import sys
                                    sys.exit()
                                
                                idx += 1
