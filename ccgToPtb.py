# ccgToPtb.py
#
# A simple program to convert the PTB to the CCGBank format for simplicity and
# easy testing of both in experiments without having to change as much code.
#

import re
import pdb
import glob

 # Point this at the PTB Corpus
PTB_DIR  = ""

# Point this at the new directory
CCG_DIR = ""

def main():
    # Grab all the files in the directory
    ptb_files = glob.glob(PTB_DIR + "/wsj_*")

    tree_count = 0  # Used as the id for each tree

    for ptb_file in ptb_files:                           # go over the ptb files
        file_name = ptb_file.split("/")[-1]         # grab the name of the file

        f = open(ptb_file, "r")
        content = f.read()                              # grab the entire file

        # A bit of a mess but splits on the start of a tree, turns it into a 1 line
        # representation of the tree
        flattened_trees = map(lambda x: re.sub("\s\s+", " ", ("( (S" + x).replace("\n", " ")),
                              content.split("( (S")[1:]
                              )

        # Write the file now in ccgbank form.
        #   ID=####
        #   ( ( S .....
        f = open(CCG_DIR + "/" + file_name, "w+")
        for tree in flattened_trees:
            f.write("ID=" + str(tree_count) + "\n")
            f.write(tree + "\n")

            tree_count = tree_count + 1         # increment for the id

        f.close()

    print "%d trees converted." % tree_count

if __name__ == "__main__":      # kick everything off, ignore
    main()
