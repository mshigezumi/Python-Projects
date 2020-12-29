import os

fpath = "/Users/mshigezumi/Documents/GitHub/Python-Projects/dir"

directory = os.listdir(fpath)

for file in directory:
    if file.lower().endswith(".txt"):
        path = os.path.join(fpath, file)
        mtime = os.path.getmtime(path)
        print(path)
        print(mtime)
