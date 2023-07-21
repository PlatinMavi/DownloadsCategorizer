import os
import shutil
import random

class DownloadCategorizer():
    def __init__(self) -> None:
        self.target = "C:/Users/PC/Downloads"
        self.exe = "C:/Users/PC/Desktop/DownloadedCategoryzer/exe"
        self.img = "C:/Users/PC/Desktop/DownloadedCategoryzer/img"
        self.zip = "C:/Users/PC/Desktop/DownloadedCategoryzer/zip"
        self.folder = "C:/Users/PC/Desktop/DownloadedCategoryzer/folder"
        self.vid = "C:/Users/PC/Desktop/DownloadedCategoryzer/vid"
        self.pdf = "C:/Users/PC/Desktop/DownloadedCategoryzer/pdf"
        self.sound = "C:/Users/PC/Desktop/DownloadedCategoryzer/sound"
        self.msi = "C:/Users/PC/Desktop/DownloadedCategoryzer/msi"
        self.uncategorized = "C:/Users/PC/Desktop/DownloadedCategoryzer/uncategorized"

    def Categorize(self):
        file_list = [file for file in os.listdir(self.target) if file != 'desktop.ini']
        # making sure to not move desktop.ini file (i dont know what it is but it is important)
        for file in file_list:
            self.Move(file)
            # itterates thru all files and folders in downloads, it then runs move function to change location

    
    def Move(self,file):
        current = self.target+"/"+file # gets the current file we are working on
        destination = self.Detect(file) # by detect function it gets its destination path

        shutil.move(current,destination)

    def Detect(self,file):
        
        if os.path.isdir(self.target+"/"+file): # checking if it is a folder, then acting accordingly
            destination = self.folder+"/"+file
        else:
            category = file.split(".")[-1].lower() # gets its file type (.exe , .png ...)

            if category == "exe":
                destination = self.exe +"/"+ file
            elif category == "zip":
                destination = self.zip+"/"+file
            elif category == "png" or category == "jpg" or category == "webp":
                destination = self.img+"/"+file
            elif category == "mp4" or category == "gif":
                destination = self.vid+"/"+file
            elif category == "pdf":
                destination = self.pdf+"/"+file
            elif category == "mp3":
                destination = self.sound+"/"+file
            elif category == "msi":
                destination = self.msi+"/"+file

            else:
                destination = self.uncategorized+"/"+file

        while os.path.exists(destination): # renames the file till it is unique
            destination = destination.split(file)[0] + str(random.randint(0,10000)) + destination.split("/")[-1]

        return destination


categorizer = DownloadCategorizer()
categorizer.Categorize()