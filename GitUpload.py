#from git import repo
from shutil import copyfile
from sys import exit
import glob
import os
import getpass
import shutil
import config

class FileUpload():

	def fileCopyLocalRepository(requiredImgFiles):
		userLocalRepo = os.mkdir(os.environ['USERPROFILE'] + "\Desktop","dummy")
		print("success")
		exit()
		for filePath in requiredImgFiles :
			print(filePath)
			destinationLocation = userLocalRepo
			try:
				shutil.copyfile(filePath, destinationLocation)
				print("File copied successfully.")
			except shutil.SameFileError: 
				print("Source and destination represents the same file.")
			except IsADirectoryError: 
				print("Destination is a directory.")
			except PermissionError: 
				print("Permission denied.")
			except: 
				print("Error occurred while copying file.")
	
	def processStart(self):
		requiredImgFiles = []
		definedFileFormat = "**/*.txt"
		currentSystemUser = getpass.getuser()
		userSourcePath = os.getcwd() #to find the user python directory
		desiredPath = userSourcePath + "\AutomationProject"
		requiredImgFiles = [f for f in glob.glob(desiredPath + definedFileFormat, recursive=False)] #to find partiular extension file format
		self.fileCopyLocalRepository(requiredImgFiles)
		exit()
	
	def gitUserLogin(self):
		print(config.gitUserCred['userName'])
		exit()	

obj = FileUpload()
data = obj.processStart()


	
