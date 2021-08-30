import os

# you can delete files over or under set by you size
target_size = 10

for source_folder, directory, files in os.walk(r'C:'):
    for file in files:
        path = os.path.join(source_folder, file)
        if os.stat(path).st_size >= target_size:#if file is bigger or smaller than target will be deleted
            os.remove(path)