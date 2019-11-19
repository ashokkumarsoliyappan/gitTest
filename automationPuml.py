from git import Repo
from shutil import copyfile
from sys import exit
import git
import glob
import os
import getpass
import shutil
import config


class gitPushPUML():

	def fileCopyLocal(self,requiredFiles,dst):
		for src in requiredFiles :
			try:
				shutil.copy2(src,dst)
				# print("File copied successfully.")
			except shutil.SameFileError: 
				print("Source and destination were the same file.")
			except IsADirectoryError: 
				print("Destination is a directory.")
			except PermissionError: 
				print("Permission denied.")
			except: 
				print("Error occurred while copying file.")
		
	def fileFormatFilter(self,desiredPath):
		requiredFiles = []
		definedFileFormat = "**/*.py"
		requiredFiles = [f for f in glob.glob(desiredPath + definedFileFormat, recursive=False)] #to find partiular extension file format
		return requiredFiles

	def localFolderCreation(self):	
		folderName = "PUMLAutomation"
		userLocalPath = os.environ['USERPROFILE'] + "\Desktop"
		folderPath = os.path.join(userLocalPath,folderName)
		if os.path.exists(folderPath):
			shutil.rmtree(folderPath)
			folderCreation = os.makedirs(os.path.join(userLocalPath,folderName))
		else:
			folderCreation = os.makedirs(os.path.join(userLocalPath,folderName))
		return folderPath
		
	def fileNameAndPath(self,localFodlerPath):
		filesCopied = self.fileFormatFilter(localFodlerPath)
		for file in filesCopied:
			filepath,fileext = os.path.split(file)
			print("Path=> {} FileName=> {} ".format(filepath,fileext))
			
	def processStart(self):
		userSourcePath = os.getcwd() #to find the user python directory
		global desiredPath
		desiredPath = userSourcePath + "\AutomationProject"
		currentSystemUser = getpass.getuser()
		# localFodlerPath = self.localFolderCreation()
		# requiredFiles = self.fileFormatFilter(desiredPath)
		# self.fileCopyLocal(requiredFiles,localFodlerPath)
		# self.fileNameAndPath(localFodlerPath)
		self.gitUserLogin(desiredPath)
		
	def deleteLocalFolder(self,localFodlerPath):
		shutil.rmtree(folderPath)

	def gitUserLogin(self,desiredPath):
		print(config.gitUserCred['userName'])
		self.gitCloneRepository()
		
	def gitCloneRepository(self):
		cloneRepository = config.gitUserCred['gitCloneUrl']
		localRepoPath = os.getcwd()
		repositoryClone = config.localGitRepository['gitLocalConfig']
		global repo
		if os.path.exists(repositoryClone):
			repo = git.Repo(config.gitUserCred['gitHubRepository'])
			print("The repository already exists")
		else:
			repository = Repo.init(localRepoPath)
			git.Git(localRepoPath).clone(cloneRepository)
			repo = git.Repo(config.gitUserCred['gitHubRepository'])
			print("repository clonned now")
		
		self.gitPull()
		self.gitAddCommit(localRepoPath)
		self.gitPush()
		
	def gitStatus(self):
		print("git Status")
	
	def gitAddCommit(self,localRepoPath):
		print("comitAdd")
		localFodlerPath = localRepoPath + "\/" + config.gitUserCred['gitHubRepository']
		requiredFiles = self.fileFormatFilter(desiredPath)
		self.fileCopyLocal(requiredFiles,localFodlerPath)
		filesCopied = self.fileFormatFilter(localFodlerPath)
		for file in filesCopied:
			print(file)
			ExtensionFile= os.path.split(file)
			fileName = os.path.splitext(ExtensionFile[1])[0]
			commitMsg = fileName + " Latest"
			repo.git.add(file)
			repo.git.commit('-m', commitMsg)
		
		
	def gitPull(self):
		origin = repo.remote(name='origin')
		origin.pull()
		
	def gitPush(self):
		repo.git.push()
		origin.push()
		
		
obj = gitPushPUML()		
obj.processStart()