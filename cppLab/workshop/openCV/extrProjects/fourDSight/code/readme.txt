############################################################################################################################
I could not find a method that I could use without converting files with .xcf extensions and output as .xcf again.
I had to convert the images to .jpg format before processing them.
#
I used converter.sh script to convert the files, gimp must be installed on the computer to use this script
#
If does not, use :
    sudo apt-get install gimp
then :
    ./converter.sh
#
############################################################################################################################
If you do not want install gimp to your system, 
Copy the files from the / sources directory to the same directory as the scripts.
############################################################################################################################
There are 3 scripts in directory:
    1 - main.py            : Python scipt for both rotated and non-rotated image
    2 - mainRotated.cpp    : C++ script for the only rotated image
    3 - mainNonRotated.cpp : C++ script for the only non-rotated image

Also there are object files of c++ codes in /cppObject directory
############################################################################################################################