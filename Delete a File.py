import os
import shutil

path = "test.txt"
#path = "doom_folder"

try:
    os.remove(path)
    #os.rmdir(path)
    #shutil.rmtree(path)
#be very careful as this deletes a directory along with all files inside
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
