import os
from tkinter import filedialog

def mergeVideo(folderPath: str, outputName: str, ext: str):
    # Get files' name in folder
    files = [file for file in os.listdir(folderPath) if file.endswith(".ts") or file.endswith(".mp4") or file.endswith(".mkv")]

    # Order the Files
    files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Get the files' absolute paths
    fileAbsolutePaths = [os.path.join(folderPath, file) for file in files]

    # Merge with ffmpeg
    mergeCode = f'ffmpeg -i "concat:{"|".join(fileAbsolutePaths)}" -c copy -bsf:a aac_adtstoasc {outputName}.{ext}'
    os.system(mergeCode)

if __name__ == "__main__":

    title = """

 /$$    /$$ /$$       /$$                           /$$      /$$                                                  
| $$   | $$|__/      | $$                          | $$$    /$$$                                                  
| $$   | $$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$       | $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
|  $$ / $$/| $$ /$$__  $$ /$$__  $$ /$$__  $$      | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
 \  $$ $$/ | $$| $$  | $$| $$$$$$$$| $$  \ $$      | $$  $$$| $$| $$$$$$$$| $$  \__/| $$  \ $$| $$$$$$$$| $$  \__/
  \  $$$/  | $$| $$  | $$| $$_____/| $$  | $$      | $$\  $ | $$| $$_____/| $$      | $$  | $$| $$_____/| $$      
   \  $/   | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/      | $$ \/  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$| $$      
    \_/    |__/ \_______/ \_______/ \______/       |__/     |__/ \_______/|__/       \____  $$ \_______/|__/      
                                                                                     /$$  \ $$                    
                                                                                    |  $$$$$$/                    
                                                                                     \______/                     
by mickimouse
"""
    print(title)
    folderPath = filedialog.askdirectory(title="Select the Videos Folder")
    while not folderPath:
        folderPath = filedialog.askdirectory(title="Select the Videos Folder")
    else:
        outputName = input("Output Name: ")
        ext = input("Extension Type (mkv, mp4 etc.): ")
        mergeVideo(folderPath, outputName, ext)