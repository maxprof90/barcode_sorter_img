
import subprocess
import os
import locale
import glob
import shutil


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

 # Нахожу все файлы в заданной папке
 folder_path = "unreadable_code"
 images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

 # Тут должен быть код, который находит файлы и копирует два элемента по времени создания
 for image in images:
    folder_name = image.

 image_files.sort(key=os.path.getmtime)

 # Код, который переносит файл из папки unreadable_code в папки со штрихкодами
 old_image_path = os.path.join(folder_path, image)
 new_image_path = os.path.join(folder, image)
 shutil.move(old_image_path, new_image_path)


 # Код, который удаляет распознанные файлы из подкаталогов, находя их по ранее присвоенному штрихкоду.

 
 
 
 