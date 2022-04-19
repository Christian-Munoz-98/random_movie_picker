import csv
import random
import webbrowser
import os

with open('2022.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def selectAlbum():
    album = data[random.randint(0,len(data))]
    return album

def main():
    while True:
        album = selectAlbum()
        print(album[0:2])
        webbrowser.open(album[2])
        webbrowser.open(album[3])
        answer = input("Another album? y/n >>>")
        if answer == "n" or answer == "N":
            break


if __name__ == "__main__":
    main()
    os.system("pause")