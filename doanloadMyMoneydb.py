from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import pickle


def main(systray):
    gauth = None
    if os.path.exists('pydrive.pickle'):
        with open('pydrive.pickle', 'rb') as token:
            gauth = pickle.load(token)
    if not gauth:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
        with open('pydrive.pickle', 'wb') as token:
            pickle.dump(gauth, token)

    drive = GoogleDrive(gauth)

    # file1 = drive.CreateFile()  # Create GoogleDriveFile instance with title 'Hello.txt'.
    # file1.SetContentFile('files/photo.jpg')
    # file1.Upload()
    file_id = 'XXX4hg6CNeAbBsUf8kPU7IB5RF4Pd-FZ'
    file1 = drive.CreateFile({'id':file_id})
    file1.GetContentFile("MyMoneyData.mdb")
    print('檔案下載成功!')