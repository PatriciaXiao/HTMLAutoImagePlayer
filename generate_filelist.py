import os

input_folder = "./img"

def is_valid_image(f):
    return f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".JPG") or f.endswith(".JPEG") or f.endswith(".PNG")

all_images = list()
 
# dirs=directories
def recursive_insert(path):
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if is_valid_image(f):
                print(root)
                print(f)
                print(path)
                break
                # all_images.
        for d in dirs:
            print(d)
            print("here!")
            recursive_insert(d)

recursive_insert(input_folder)

