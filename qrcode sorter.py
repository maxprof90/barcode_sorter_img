
import subprocess
import os
import locale
import glob


encoding = locale.getdefaultlocale()[1]

def get_code(file):

	try:
		raw_code = subprocess.check_output(["C:\\Program Files (x86)\\ZBar\\bin\\zbarimg", "-q", \
		file])
		raw_code = raw_code.rstrip()
		raw_code = raw_code.decode(encoding)
		code = raw_code.split(':',1)[1]
		return(code)
	except:
		return("")


image_files=glob.glob('*.JPG') + glob.glob('*.png')
print(image_files)

for file in image_files:

 file_path = os.path.join(os.getcwd(), file) 

 code = get_code(file)

 folder = os.path.join(os.getcwd(), code)
 os.makedirs(folder, exist_ok=True)

 os.rename(file_path, folder)
 
 # Если папке присвоен код переименовать два файла идущих следующими и скопировать в папку.
 # Иначе переместить 3 файла в папку unreadable_code
 