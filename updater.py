import zipfile
import os
import urllib.request
import shutil
from time import sleep

print("FerSReD Nuker güncelleniyor, lütfen bekleyin...")
os.system("title FerSReD Nuker güncelleniyor lütfen bekleyin...")

print("Nuker süreci kapatılıyor...")
os.system('taskkill /f /im fersred-nuker.exe')

sleep(2)

os.remove("fersred-nuker.exe")
shutil.rmtree("_internal")

print("Downloading release.zip...")
urllib.request.urlretrieve("https://github.com/FerSReD98/fersred-nuker/raw/Rework/release.zip", "release.zip")

with zipfile.ZipFile("release.zip", "r") as release:
    release.extractall()

os.remove("release.zip")
os.remove("updater.zip")

os.system("fersred-nuker.exe")
