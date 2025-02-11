from PIL import Image
from PIL import ImageFilter
from urllib.request import urlopen

def change_type(oldImage):
    change = input("Do you want to change the file type?").upper()
    # Save the image in a different format
    if change == "YES":
        newName = input("type in the new name of the image and the new type(format: filename.type)")
    # only works if file type in name is spelled correct!!
    elif change == "NO":
        newName = input("Please type in the name you want the image to be saved as")
    oldImage.save(newName)

def rotate(oldImage):
    deg = int(input("How many degrees do you want to rotate (counter-clockwise)?"))
    # CHECK FOR ERROR
    rotated = oldImage.rotate(deg)
    rotated.show()
    return rotated

def resize(oldImage):
    width = input("What width should your image have?")
    length = input("What length should your image have?")
    resized = oldImage.resize((width, length))
    resized.show()
    return resized
    # WIDTH AND LENGTH SWAPPPED?

def merge_bands(oldImage):
    r, g, b = oldImage.split()
    merged = Image.merge("RGB", (b, g, r))
    merged.show()
    return merged
    # ALL BLACK TO WHITE??

def apply_filter(oldImage):
    filtered = oldImage.filter(ImageFilter.DETAIL)
    filtered.show()
    return filtered
    # OTHER FILTERS??

while True:
    name = "dog.jpg"
    im = Image.open(name)
    # kind = input("Do you have your picture saved locally or from the internet?")
    # if kind == "locally":
    #     name = input("type in the name of your file")
    #     im = Image.open(name)
    # elif kind == "internet":
    #     url = input("copy the url of your selected picture here:")
    #     im = Image.open(urlopen(url))
    # else:
    #     print("invalid input")
    print("this is the file type and the size of your selected image")
    print(im.format, im.size)
    inp = input("If you want to edit your image type 'edit', if you want to save your file type 'save'")
    if inp == 'edit':
        edit = input("Do you want to ...?")
        if edit == "resize":
            im = resize(im)
            continue
        if edit == "rotate":
            im = rotate(im)
            continue
        if edit == "filter":
            im = apply_filter(im)
            continue
        if edit == "color":
            im = merge_bands(im)
            continue
    elif inp == 'type':
        change_type(im)
        break
im.show()
