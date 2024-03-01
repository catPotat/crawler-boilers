import os
import shutil

USER_PATH = os.environ['USERPROFILE']
CACHE_PATH = 'AppData/Roaming/Discord/Cache'
DESKTOP = 'Desktop'

SOURCE = os.path.join(USER_PATH, CACHE_PATH)
DESTINATION = os.path.join(USER_PATH, DESKTOP)

print(SOURCE)
print(DESTINATION)


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    try:
        path = shutil.move(SOURCE, DESTINATION)
    except:
        pass
    path = DESTINATION + '/Cache/'
    print(path)
    for filename in os.listdir(path):
        ext = os.path.splitext(filename)[1].lower()
        if not ext:
            print(filename)
            source = path + filename
            dest = path + filename+".png"
            os.rename(source, dest)
      
if __name__ == '__main__':
    # input("'Enter' to recover discord deleted pics")
    main()
