# ccgToPtb.py
#
# A simple program to convert the PTB to the CCGBank format for simplicity and
# easy testing of both in experiments without having to change as much code.
#
# Directions for use:

import pdb
import glob
import re

 # Point this at the PTB Corpus
PTB_DIR  = "/Users/matthewebeweber/Documents/DAN/combined"

# Point this at the new directory
CCG_DIR = "/Users/matthewebeweber/Documents/DAN/ccg_converted"

def main():
    # Grab all the files in the directory
    ptb_files = glob.glob(PTB_DIR + "/wsj_*")
    tree_count = 0

    for ptb_file in ptb_files:
        file_name = ptb_file.split("/")[-1]

        f = open(ptb_file, "r")
        content = f.read()

        flattened_trees = map(lambda x: re.sub("\s\s+", " ", ("( (S" + x).replace("\n", " ")),
                              content.split("( (S")[1:]
                              )

        f = open(CCG_DIR + "/" + file_name, "w+")
        for tree in flattened_trees:
            f.write("ID=" + str(tree_count) + "\n")
            tree_count = tree_count + 1

            f.write(tree + "\n")

        f.close()

    print "%d trees converted." % tree_count







if __name__ == "__main__":
    main()
