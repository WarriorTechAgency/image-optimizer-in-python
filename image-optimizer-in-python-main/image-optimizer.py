from tabulate import tabulate
from PIL import Image
import argparse
import os
from colorama import init, Fore
import time
import sys
import itertools
import datetime as dt
import shutil


black = Fore.BLACK
reset = Fore.RESET
yellow = Fore.YELLOW
blue = Fore.BLUE
red  = Fore.RED
green  = Fore.GREEN
init()

class ImageCompressor:
    def get_input(self):
        os.system("clear")

        print(f"{green}[*] To use this compressor, you will need to group the images you wish to compress in on folder and it should be in the same diretory as the imageCompressor.py{reset}")
        time.sleep(.4)
        self.name = input(f"\n {blue}Enter the name of the directory?\n-$> {reset}")
        time.sleep(.4)
        create_directory = input(f"\n {blue}Enter the directory you want to keep them. \n-$> {reset}")
        time.sleep(.4)
        try:
            os.mkdir(create_directory)
        except FileExistsError as e:
            print(f"{e} {self.name} already exist")

        time.sleep(.2)
        isExist = os.path.exists(self.name)
        if isExist:
            dir_lists = os.listdir(self.name)
            images = []
            for list in dir_lists:
                images.append(f'{list}')
            
            num = 0
            data=[]
            result =[]
            head1 = ["Name", 'Size', 'Time']
            head2 = ["Name", 'Size', 'Time']
            self.loadImage("Loading images from ", "loaded images from")
            
            
            files = []
            date_time = dt.datetime.now()
            for image in images:
                with Image.open(f'{self.name}/{image}') as img:
                    (width, height)  = img.size
                    new_size = (width//2, height//2)
                    new_image = img.resize(size=new_size)
                    num += 1
                    fileName, extention = os.path.splitext(image)

                    data.append( [
                        fileName+f"-{width}x{height}"+extention, img.size, f"{date_time.hour}:{date_time.minute}:{date_time.second}"
                    ])

                    result.append([
                        f"{create_directory}-{num}-{new_image.size[0]}x{new_image.size[1]}{extention}", new_image.size, f"{date_time.hour}:{date_time.minute}:{date_time.second}"
                    ])

                    new_image.save(f"{create_directory}-{num}-{new_image.size[0]}x{new_image.size[1]}{extention}",optimize=True, quantity=50)

                    files.append(f"{create_directory}-{num}-{new_image.size[0]}x{new_image.size[1]}{extention}")

            self.loadImage("Saving compressed images to '/directory'", "Saved")
            
            
            for file in files:
                shutil.move(file, create_directory)
            
            print(f"\nUncompressed image(s) in {self.name} \n"+"-"*70)
            print("\n",tabulate(data, headers=head1, tablefmt="grid"))
            print(f"\nCompressed image(s) in {self.name} \n"+"-"*70)
            print("\n",tabulate(result, headers=head2, tablefmt="grid"))         
        else:
            print("check and try again!".title(), f"/{self.name} Directory dosen't exist.")
        


    def loadImage(self, text, past_text ):
        done = 0
        for x in itertools.cycle(["|", "/", "-", "\\"]):
            if done == 20:
                break
            sys.stdout.write(f"\r[{x}] {text} {self.name}... ")
            sys.stdout.flush()
            time.sleep(.2)
            done += 1

        sys.stdout.write(f"\r\n[+] {past_text} \n")
        

try:
    ImageCompressor().get_input()
    
except KeyboardInterrupt as e:
    print(f"\n\n {red}[!]{e} CTRL + C have been detected..\n\n [!] Exiting... {reset}")
