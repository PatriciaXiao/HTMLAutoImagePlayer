import os

input_folder = "./img"
out_file = "my_helper.js"

def is_valid_image(f):
    return f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".JPG") or f.endswith(".JPEG") or f.endswith(".PNG")

def has_valid_year(name):
    valid_numbers = [str(i) for i in range(10)]
    year_digits = 4
    for i in range(year_digits):
        if name[i] not in valid_numbers:
            return False
    return True

def has_valid_date(name):
    valid_numbers = [str(i) for i in range(10)]
    date_digits = 8
    for i in range(date_digits):
        if name[i] not in valid_numbers:
            return False
    return True

all_images = list()
all_names = list()
all_times = list()

for (root, dirs, file) in os.walk(input_folder):
    for f in file:
        if is_valid_image(f):
            all_images.append(os.path.join(root, f))

            suffix = f.split(".")[-1]
            raw_name = f[:-len(suffix)-1]

            folder = root.split("/")[-1]
            
            if has_valid_year(raw_name):
                if has_valid_date(raw_name):
                    time = raw_name[:8]
                    name = folder + ": " + raw_name[8:]
                else:
                    time = raw_name[:4]
                    name = folder + ": " + raw_name[4:]
            else:
                assert False, "There is an invalud file {0}".format(os.path.join(root, f))

            all_names.append(name)
            all_times.append(time)

all_sorted = sorted(zip(all_times,all_names,all_images))

all_images = [x for _,_,x in all_sorted]
all_names  = [x for _,x,_ in all_sorted]

image_list_str = ",".join(["\"{0}\"".format(img) for img in all_images])
label_list_str = ",".join(["\"{0}\"".format(nms) for nms in all_names])

with open(out_file, "w") as f:
    f.write("var ImageList = [{0}];\nvar LabelList = [{1}];".format(image_list_str, label_list_str))

