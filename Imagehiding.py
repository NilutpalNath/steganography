from PIL import Image
from tkinter import filedialog
import os

def imagedata():
        open_return = filedialog.askopenfilename(initialdir="C:\\", title="Open image to hide", defaultextension=".png", filetypes=[("Images", "*.png"), ("All Files", "*.*")])
        imgpath = os.path.abspath(open_return)
        img = Image.open(imgpath)
        datas = img.getdata()
        message = ''
        for item in datas:
                message = message + '{:08b}'.format(item[0]) + '{:08b}'.format(item[1]) + '{:08b}'.format(item[2])
        return [message, '{:010b}'.format(img.height), '{:010b}'.format(img.width)]

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
    hexcode = hexcode.lstrip('#')
    lv = len(hexcode)
    return tuple(int(hexcode[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def formimage(binary, stegloc):
        imData = []
        
        width = int(binary[-10:], 2)
        height = int(binary[-20:-10], 2)
        binary = binary[:-20]
        while(binary):
                r, g, b = tuple(int(binary[i:i+8], 2) for i in range(0, 24, 8))
                imData.append((r,g,b,255))
                binary = binary[24:]

        img = Image.new('RGB', (width, height))
        img.putdata(imData)
        retrievedimg = stegloc.strip(os.path.basename(stegloc)) + "\\output.png"
        img.save(retrievedimg, "PNG")
        img.show()


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

def imageHide():

    message, height, width = imagedata()
    cover = filedialog.askopenfilename(initialdir="C:\\", title="Open cover image", defaultextension=".png", filetypes=[("Images", "*.png"), ("All Files", "*.*")])

    img = Image.open(cover)
    binary = message + height + width + '1111111111111111111111111111111111110'
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
        stagimg = cover.strip(os.path.basename(cover)) + "\\newstaged.png"
        img.save(stagimg, "PNG")
        img.show()
    else:
        return "Incorrect Image mode, couldn't hide"

def imageRetrieve():
    retrimg = filedialog.askopenfilename(initialdir="C:\\", title="Open stego image", defaultextension=".png", filetypes=[("Images", "*.png"), ("All Files", "*.*")])
    
    img = Image.open(retrimg)
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
                
                if (binary[-37:] == '1111111111111111111111111111111111110'):
                    formimage(binary[:-37], retrimg)
                    return
