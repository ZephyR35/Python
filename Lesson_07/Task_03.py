from os.path import join
from shutil import copytree,rmtree
import os

path_old = join('.','Task_03','my_project')
path_new = join('.','Task_03','my_project','templates')
copytree(path_old,path_new)
rmtree(join('.','Task_03','my_project','settings'))
rmtree(join('.','Task_03','my_project','miniapp'))
rmtree(join('.','Task_03','my_project','authapp'))






