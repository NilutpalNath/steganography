from PIL import Image
import binascii
import optparse
from tkinter import filedialog
import os
import inmsg 



def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
    hexcode = hexcode.lstrip('#')
    lv = len(hexcode)
    return tuple(int(hexcode[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def str2bin(message):
    binary = bin(int(binascii.hexlify(message), 16))
    return binary[2:]

def bin2str(binary):
    message = binascii.unhexlify('%x' % (int(binary,2)))
    return message

def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
            hexcode = hexcode[:-1]+digit
            return hexcode
    else:
            return None

def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
            return hexcode[-1]
    else:
            return None

def textHide():

    cover = filedialog.askopenfilename(initialdir="C:\\", title="Open cover image", defaultextension=".png", filetypes=[("Images", "*.png"), ("All Files", "*.*")])
    img = Image.open(cover)
    binary = str2bin(inmsg.insert().encode()) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        digit = 0
        
        for item in datas:
            if (digit < len(binary)):
                newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
                
                if newpix == None:
                    newData.append(item)
                else:
                    r, g, b = hex2rgb(newpix)
                    newData.append((r,g,b,255))
                    digit += 1
            else:
                newData.append(item)
        img.putdata(newData)
        stagimg = cover.strip(os.path.basename(cover)) + "\\textstaged.png"
        img.save(stagimg, "PNG")
        img.show()
    else:
        return "Incorrect Image mode, couldn't hide"

def textRetrieve():
    open_return = filedialog.askopenfilename(initialdir="C:\\", title="Open stego image", defaultextension=".png", filetypes=[("Images", "*.png"), ("All Files", "*.*")])
    
    filename = retrimg = os.path.abspath(open_return)
    img = Image.open(filename)
    binary = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:
            digit = decode(rgb2hex(item[0], item[1], item[2]))
            if digit == None:
                pass
            else:
                binary = binary + digit
                
                if (binary[-16:] == '1111111111111110'):
                    binary = '0b'+binary[:-16]
                    inmsg.displaymsg(bin2str(binary).decode())
                    break;
            
    else:
        return "Incorrect Image mode, couldn't retrieve"

