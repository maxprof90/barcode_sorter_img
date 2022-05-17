
import subprocess
import os
import locale
import glob


encoding = locale.getdefaultlocale()[1]
# Распознаю штрихкод
def get_code(file):

	try:
		raw_code = subprocess.check_output(["C:\\Program Files (x86)\\ZBar\\bin\\zbarimg", "-q", \
		file])
		raw_code = raw_code.rstrip()
		raw_code = raw_code.decode(encoding)
		code = raw_code.split(':',1)[1]
		return(code)
	except:
		return("unreadable_code")


image_files=glob.glob('*.JPG') + glob.glob('*.png')
print(image_files)

for file in image_files:

 file_path = os.path.join(os.getcwd(), file) 

 code = get_code(file)

 # Создаю папку и присваиваю имя штрихкода
 folder = os.path.join(os.getcwd(), code)
 os.makedirs(folder, exist_ok=True)

 # Распределяю файлы по папкам, присваиваю штрихкод в имя файла для дальнейшей привязки
 os.rename(file_path, folder + file)

		
 # 1. Запускаю цикл перебора файлов в папке "unreadable_code". Скопировать первые два файла в первую папку
		# поиск осуществлять по времени создания файла.
 # 2. Удаляю распознанные файлы из подкаталогов, находя их по ранее присвоенному штрихкоду.

 
 
 
 