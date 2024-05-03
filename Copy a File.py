#the shutil module offers 3 functions:
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #there are two arguments: src,dst (source, destination)
#since the test file is in the project folder, I don't need to list the full path
# just the file name is enough