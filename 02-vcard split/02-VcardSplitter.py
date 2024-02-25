import re
import os

#open and read source multiple VCARD file
sourcefile = open("kontakty.vcf", "r")
source = sourcefile.read()
sourcefile.close

#split contacts by BEGIN:VCARD string
vcards = re.split('(?=BEGIN:VCARD)', source)

number = 0
#name of target folder for each vcards
folder = "cards"

#create target folder if not exist
if not os.path.exists(folder):
    os.mkdir(folder)

#count each contacts in multiplecard
length = len(vcards)

#create single vcards
for i in range(length):
    if i != 0:
        number = i
        findname = re.findall(r'FN;CHARSET=utf-8:(.*?)\n', vcards[i])
        cardname = findname[0]
        cardname = cardname.replace(" ", "-", 1)
        cardname = cardname.replace(" ", "")

        file = open(f"{folder}/{number}-{cardname}.vcf", "w")
        file.write(vcards[i])
        file.close()            