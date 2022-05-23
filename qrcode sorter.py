import os
import subprocess
import glob
from math import ceil, floor

folder_address = os.path.abspath(os.curdir) # адрес папки
directory = os.fsencode(folder_address)
i = 0
files_in_folder = 3 # можно менять значение, сколько файлов должно быть в папке.

# на данный момент ищет все файлы. Нужно сделать, чтобы выбирал только файлы jpg
num_of_files = num_of_files = len([name for name in os.listdir(directory)  if  os.path.isfile(os.path.join(directory, name))]) 



for x in range(ceil(num_of_files / files_in_folder)): 
    path = folder_address + "\\" + str(x + 1) 
    if not os.path.exists(path):
        os.mkdir(path)

files = (file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))) 
for file in files:
   
    file_name = os.fsdecode(file)
    file_path = os.path.join(folder_address, file_name)
    new_file_path = os.path.join(folder_address, str(floor(i / files_in_folder) + 1), file_name)
    os.rename(file_path, new_file_path)
    i += 1



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

 # Распределяю файлы по папкам, присваиваю штрихкод
 os.rename(file_path, folder + file)

 # Тут должен быть код, который удалит файлы со штрихкодом

 

 
 
 
 