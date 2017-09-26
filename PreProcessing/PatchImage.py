from PIL import Image
import os


def get_files(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name))]

Image.MAX_IMAGE_PIXELS = None

d = get_files('/home/kavya/Data/Data1/GT1/')
fileCounter = 0
patchCounter = 0
for k in range(0, len(d)):
    f = d[k][:-4]
    nameGT = "/home/kavya/Data/Data1/GT1/" + f + ".png"
    nameAP = "/home/kavya/Data/Data1/AP1/" + f + ".png"
    if (os.path.exists(nameGT) and os.path.exists(nameAP)):
        print(f)
        imgGT = Image.open(nameGT)
        imgAP = Image.open(nameAP)
        width = imgGT.size[0]
        height = imgGT.size[1]

        numW = width // 512
        numH = height // 512
        print(nameGT + " Files: " + str(fileCounter) + " Patches: " + str(patchCounter))
        counter = 0
        for i in range(0, numW):
            for j in range(0, numH):
                left = 512 * i
                right = 512 * (i + 1)
                upper = 512 * j
                lower = 512 * (j + 1)
                # left upper right lower
                patchGT = imgGT.crop((left, upper, right, lower))
                patchAP = imgAP.crop((left, upper, right, lower))
                patchGTGrey = patchGT.convert('L')
                pix = patchGTGrey.load()
                nblack = 0
                widthT, heightT = patchGTGrey.size
                for x in range(0, widthT):
                    for y in range(0, heightT):
                        if (pix[x, y] > 250):
                            nblack += 1
                if (nblack / float(widthT * heightT) < 0.1):
                    print("\tyay! less than 10% black. " + str(patchCounter))
                    # patchGT.show()
                    # patchAP.show()
                    if(widthT == 512 and heightT == 512):
                        patchAP.save("/home/kavya/Data/Data1/FeatureImage/" + f + "_" + str(i) + "_" + str(j) + ".png",'PNG')
                        patchGT.save("/home/kavya/Data/Data1/LabelImage/" + f + "_" + str(i) + "_" + str(j) + ".png", 'PNG')
                        patchCounter += 1
                    # else:
                    # print("\tno! more than 70% black")
        fileCounter += 1
    else:
        print("FILE DOES NOT EXIST. " + nameGT)