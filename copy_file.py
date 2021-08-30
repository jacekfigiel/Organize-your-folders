from pathlib import Path
import shutil
import os
# you can move specific type of file using this program

source_folder = r"C:"
target_folder = r"C:"


for file_name in Path(source_folder).glob("*.txt"):#you can chnage file type
    shutil.move(os.path.join(source_folder,file_name), target_folder)