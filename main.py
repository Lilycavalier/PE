from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

name = "dog.jpg"
im = Image.open(name)
# from urllib.request import urlopen
# kind = input("Do you have your picture saved locally or from the internet?")
# if kind == "locally":
#     name = input("type in the name of your file")
#     im = Image.open(name)
# elif kind == "internet":
#     url = input("copy the url of your selected picture here:")
#     im = Image.open(urlopen(url))
# else:
#     print("invalid input")
print("this is the file type, the size and the mode of your selected image")
print(im.format, im.size, im.mode)
while True:
    inp = input("If you want to edit your image type 'edit', if you want to change your file type type 'type', if you're done editing type 'done'")
    if inp == 'edit':
        edit = input("Do you want to ...?")
        if edit
    elif inp == 'type':
        # Save the image in a different format
        options = []  # !!
        newName = input("type in the new name of the image (format: name.type)")
        # only works if file type in name and in type are equal
        newType = upper(input("type in the new file type or type 'OPTIONS' to see available options"))
        if newType == "OPTIONS":
            print(options)
            newType = input("Now type in the type you want to change your image to")
        if newType not in options:
            newType = input("This type is not available. Choose a different one.")
        im.save(newName, newType)

# out.show()
