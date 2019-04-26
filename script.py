# %%
import os
import shutil
import subprocess
import sys
from glob import glob


os.chdir('..')
orig_dir = os.getcwd()
# %%
os.system(' git clone https://github.com/kushalchordiya216/ADSL')
os.chdir('ADSL')
# %%
if(int(sys.argv[1]) <= 9):
    with open(f'srcfile/ADSL{sys.argv[1]}.cpp', "r") as file:
        data = file.read()
    os.chdir(orig_dir)
    with open(f'{sys.argv[2]}.cpp', 'w') as file:
        file.write(data)
elif(sys.argv[1] == '13'):
    with open(f'srcfile/ADSL{sys.argv[1]}.java', "r") as file:
        data = file.read()
    os.chdir(orig_dir)
    with open(f'{sys.argv[2]}.java', 'w') as file:
        file.write(data)
else:
    os.chdir(orig_dir)
    os.mkdir(f'{sys.argv[2]}')
    command = 'cp -r ./ADSL/srcfile/ADSL'+sys.argv[1]+'/. ./'+sys.argv[2]
    os.system(command)

# %%
shutil.rmtree('ADSL', ignore_errors=True)
os.system('clear')
shutil.rmtree('Scripts', ignore_errors=True)
