import os
import shutil
from PIL import Image

class ImageConverter():
    os.system("clear")
    def getExtension(self):
        extension = input("What extension are you converting to? [PNG/JPEG/JPG] \n-$>\t ".upper())
        ext = ["png", "jpeg", "jpg"]
        while extension.lower() not in ext:
            
            extension = input("What extension are you converting to? [PNG/JPEG/JPG] \n-$>\t ")
            
        else:
            print(f"[+] Selected: {extension.upper()}")
            return extension
        
    def getFiles(self):
        print("[+] The file(s) you are converting should be in one directory.\n[+] And it should be in the same directory as the convert file")
        directory = input("Enter the directory: \n-$>\t ".upper())
        
        if not os.path.exists("convertor"):
            os.mkdir("convertor")
          
        while os.path.isdir(directory) == False:
            directory = input("Enter the directory: \n-$>\t ")
        else:
            extension = self.getExtension()
            files = os.listdir(directory) 
            file_data = []
            ext = ["png".upper(), "jpeg".upper(), "jpg".upper()]
            num = 0
            for file in files:
                num+=1
                file_data.append(f"{directory}/{file}")
                with Image.open(f"{directory}/{file}") as image:
                    x = os.path.splitext(file)
                    image.save(f"{x[0]}[converted].{extension}")
                    size = image.size()
                    shutil.move(f"{x[0]}-{size[0]}x{size[1]}.{extension}", "convertor")
            
try:
    ImageConverter().getFiles()
except KeyboardInterrupt as e:
    print(f"{e}\n\n CTRL + C have been detected..\n\n [!] Exiting... ")