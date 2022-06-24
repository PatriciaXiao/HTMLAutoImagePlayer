# HTMLAutoImagePlayer
 The HTML Auto Image Player I use for my wedding.

## Steps To Use

1. Add Your Images under the [img](./img) subfolder
    * It doesn't matter if you have folders under folders. We can handle it in the next step.
    * Names has to be in the format of [date/time]+[tag], e.g. **20220623Picnic.jpg**, or **2022Memory.jpg**. Only 8-digit number date and 4-digit year can be accepted and automatically processed. Otherwise please edit the Python script for your need.
2. Run the Python script [generate_filelist.py](./generate_filelist.py) to generate new data list file **my_helper.js**
3. Open [my_demo.html](./my_demo.html) in your browser (e.g. Chrome)

## Toy Sample

There is a hard-coded toy sample available. You can access it by simply open [sample_my_demo.html](./sample_my_demo.html) in the browser.

