from PIL import Image
import os


#MGMT positive- 7,39,10,38
#1,12,39-classical, 6,7-mesenchymal, 9,19,10,38-proneural, 40,48-neural
#MGMT neg- 1, 6, 9, 19, 48

def get_files(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name))]


Image.MAX_IMAGE_PIXELS = None

d = get_files('/home/kavya/Data/Data3/')
fileCounter = 0
patchCounter = 0
sectionCounter = [0, 0, 0, 0]
print(len(d))
for k in range(0, len(d)):
    print(d[k])
    if ('AP' in d[k]):
        f = d[k][:-7]
        nameGT = "/home/kavya/Data/Data3/" + f + "_GT.jpg"
        nameAP = "/home/kavya/Data/Data3/" + f + "_AP.jpg"
        if (os.path.exists(nameGT) and os.path.exists(nameAP)):
            imgGT = Image.open(nameGT)
            imgAP = Image.open(nameAP)
            width = imgGT.size[0]
            height = imgGT.size[1]

            numW = width // 256
            numH = height // 256
            print(nameGT + " Files: " + str(fileCounter) + " Patches: " + str(patchCounter))
            counter = 0
            for i in range(0, numW):
                for j in range(0, numH):
                    left = 256 * i
                    right = 256 * (i + 1)
                    upper = 256 * j
                    lower = 256 * (j + 1)
                    # left upper right lower
                    patchGT = imgGT.crop((left, upper, right, lower))
                    patchAP = imgAP.crop((left, upper, right, lower))
                    patchGTGrey = patchGT.convert('L')
                    pix = patchGTGrey.load()
                    nblack = 0
                    widthT, heightT = patchGTGrey.size
                    for x in range(0, widthT):
                        for y in range(0, heightT):
                            if (pix[x, y] == 124):
                                nblack += 1
                    if (nblack / float(widthT * heightT) < 0.1):
                        # patchGT.show()
                        # patchAP.show()
                        if (widthT == 256 and heightT == 256):
                            if (("W7" in f) or ("W39" in f) or ("W10" in f) or ("W38" in f)):
                                patchAP.save("/home/kavya/Data/Data3/Input/MGMT+/" + f + "_" + str(i) + "_" + str(j) + ".png", 'PNG')
                                # patchGT.save("/home/kavya/Data/Data3/Input/MGMT+/" + f + "_" + str(i) + "_" + str(j) + ".png", 'PNG')
                                sectionCounter[0] += 1
                            elif (("W6" in f) or ("W1" in f) or ("W19" in f) or ("W9" in f) or ("W48" in f)):
                                patchAP.save("/home/kavya/Data/Data3/Input/MGMT-/" + f + "_" + str(i) + "_" + str(j) + ".png", 'PNG')
                                # patchGT.save("/home/kavya/Data/Data3/Input/MGMT-/" + f + "_" + str(i) + "_" + str(j) + ".png", 'PNG')
                                sectionCounter[1] += 1
                            patchCounter += 1
                        print("\t File: " + str(fileCounter) + ". yay! less than 10% non-cellular tumor. " + str(patchCounter) + ". MGMT+: " + str(sectionCounter[0]) + ". MGMT-: " + str(sectionCounter[1]) + ".")
            fileCounter += 1