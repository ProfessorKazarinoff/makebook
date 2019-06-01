# images.py

import os
import re
import sys
import shutil


def copy_all_images_to_dir(notebook_dir_name="notebooks", images_dir="images"):
    """
    a function to copy the all of the images out of notebooks/subdir/images into
    one big folder in pdf/images
    """
    nb_dir = os.path.join(os.pardir, notebook_dir_name)
    images_dir = os.path.join(os.pardir, "pdf", images_dir)
    REG_nb_dir = re.compile((r"(\d\d)-*"))

    # erase the /pdf/images dir if it exists
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)

    # create a new empt /pdf/images dir
    os.makedirs(os.path.join(os.pardir, "pdf", "images"))

    for dir in os.listdir(nb_dir):
        if REG_nb_dir.match(dir):
            if os.path.exists(os.path.join(nb_dir, dir, "images")):
                scr_dir = os.path.join(nb_dir, dir, "images")
                for f in os.listdir(scr_dir):
                    try:
                        shutil.copy(
                            os.path.join(scr_dir, f),
                            os.path.join(os.pardir, "pdf", "images"),
                        )
                    except IOError as e:
                        print("Unable to copy file. %s" % e)
                        exit(1)
                    except:
                        print("Unexpected error:", sys.exc_info())
                        exit(1)

            # else:
            # print("no images folder in directory: {}".format(str(dir)))
