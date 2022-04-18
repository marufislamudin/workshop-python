# fungsi untuk berinteraksi dengan sistem operasi
import os
os.getcwd()
os.chdir('/server/accesslogs')
os.system('mkdir today')

# Built-in dir()dan help() 
# berguna sebagai alat bantu interaktif 
# untuk bekerja dengan modul besar seperti os:
import os
dir(os)
help(os)

# library shutil 
# untuk tugas manajemen file dan direktori harian
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')