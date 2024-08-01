import os
files=os.listdir("FolderName")
i=1
for file in files:
    if file.endswith(".(extension)"):
        os.rename(f"Foldername/{file}",f"Foldername/{i}.png")
        i+=1
