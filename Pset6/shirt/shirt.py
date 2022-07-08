from posixpath import splitext
from PIL import Image, ImageOps, ImageDraw
import sys

def main():
    command_line_arg()
    



def command_line_arg():
    if len(sys.argv) < 3:
        print('Too few command-line argument')
        sys.exit()
    elif len(sys.argv) > 3:
        print('Too many command-line argument')
        sys.exit()
    else:
        convert()

def check_extn():
    root, in_ext = splitext(sys.argv[1])
    root, out_ext = splitext(sys.argv[2].lower())

    if out_ext not in [".jpg",'.png']:
        print("invalid Output")
        sys.exit()
    elif in_ext != out_ext:
        print("Input and output have different extensions")
        sys.exit()
        

        
def convert():
    if len(sys.argv) == 3:
        try:
            imagefile = Image.open(sys.argv[1])
            # return imagefile  
        except FileNotFoundError:
            print("Input does not exist")
            sys.exit()
        check_extn()
        shirtfile = Image.open("shirt.png")
        size = shirtfile.size

        
        muppet = ImageOps.fit(imagefile,size)
        muppet.paste(shirtfile,shirtfile)
        muppet.save(sys.argv[2].lower())

if __name__ == "__main__":
    main()
