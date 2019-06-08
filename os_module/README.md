#OS module provides a way of using operating system dependent functionality

import os 

#Execute a shell command
os.system()

#Get the users environment
os.environ()

#Returns the current working directory
os.getcwd()

#Returns the current process's user id
os.getuid()

#Returns the real process id of the current process
os.getpid()

#Return information identifying the current operating system
os.uname()

#Change the root directory of the current process to path
os.chroot(path)

#Return a list of the entries in the directory given by path
os.listdir(path)

#Create a directory named path with numeric mode  mode
os.mkdir(path)

#Recursive directory creation function
os.mkdirs(path)

#Remove/Delete the file path
os.remove(path)

#Removes directories recursively
os.removedirs(path)

#Rename the file of directory
os.rename(src, dst)

#Remove/delete the directory path
os.rmdir(path)