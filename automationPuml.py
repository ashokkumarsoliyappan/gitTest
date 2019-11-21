from git import Repo,Commit
# from shutil import copyfile
from datetime import datetime
from sys import exit
import git
import glob
import os
import getpass
import shutil
import config
import xlsxwriter
import logging

class gitPushPUML():

	errorLogFormat = "%(asctime)s:::%(filename)s:::%(lineno)d:::%(message)s"
	logFormat = "%(asctime)s:::%(filename)s:::%(message)s"
	logging.basicConfig(filename=config.LOGFIleNAME,level=logging.DEBUG, format = logFormat)
	logging.basicConfig(filename=config.LOGFIleNAME,level=logging.error, format = errorLogFormat)

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
		global desiredPath
		userSourcePath = os.getcwd() #to find the user directory
		desiredPath = userSourcePath + "\AutomationProject"
		currentSystemUser = getpass.getuser()
		# localFodlerPath = self.localFolderCreation()
		# requiredFiles = self.fileFormatFilter(desiredPath)
		# self.fileCopyLocal(requiredFiles,localFodlerPath)
		# self.fileNameAndPath(localFodlerPath)
		logging.info("================>ProcessStarted<================")
		self.gitUserLogin(desiredPath)
		exit()
		
	def deleteLocalFolder(self,localFodlerPath):
		shutil.rmtree(folderPath)

	def gitUserLogin(self,desiredPath):
		print(config.gitUserCred['userName'])
		self.gitCloneRepository()
		
	def gitCloneRepository(self):
		localRepoPath = os.getcwd()
		cloneRepository = config.gitUserCred['gitCloneUrl']
		repositoryClone = config.localGitRepository['gitLocalConfig']
		global repo,head
		if os.path.exists(repositoryClone):
			repo = git.Repo(config.gitUserCred['gitHubRepository'])
			# print(config.repoClonnedExist)
			logging.debug(config.repoClonnedExist)
		else:
			repository = Repo.init(localRepoPath)
			git.Git(localRepoPath).clone(cloneRepository)
			repo = git.Repo(config.gitUserCred['gitHubRepository'])
			print(config.repoClonnedSuccessMsg)
			logging.debug(config.repoClonnedSuccessMsg)
		self.gitPull()
		modifiedFiles,gitFileName,commitID = self.gitAddCommit(localRepoPath)
		self.gitPush()
		self.gitUrlFormation(modifiedFiles,gitFileName,commitID)
		
	def gitStatus(self):
		print("git Status")
	
	def gitAddCommit(self,localRepoPath):
		print("comitAdd")
		modifiedFiles,gitFileName,filenameForm,commitID =[],[],[],[]
		localFodlerPath = localRepoPath + "\/" + config.gitUserCred['gitHubRepository']
		requiredFiles = self.fileFormatFilter(desiredPath)
		self.fileCopyLocal(requiredFiles,localFodlerPath)
		filesCopied = self.fileFormatFilter(localFodlerPath)
		for file in filesCopied:
			ExtensionFile= os.path.split(file)
			fileName = os.path.splitext(ExtensionFile[1])[0]
			commitMsg = fileName + " Latest"
			repo.git.add(file)
			gitFileName.append(ExtensionFile[1])
			try:
				repo.git.commit('-m', commitMsg)
				head = repo.heads[0]
				commitID.append(head.commit)
				filenameForm.append(ExtensionFile[1])
				modifiedFiles.append(file)
			except git.exc.GitCommandError:
				print("There is no changes made in the file/Already in the github  repository")
		return filesCopied,gitFileName,commitID
		 
	def gitPull(self):
		try :
			global origin		
			origin = repo.remote(name='origin')
			origin.pull()
			logging.debug("Successfully Pulled the changes from the remote{{}} repository".format(config.gitUserCred['gitHubRepository']))
		except exception as e:
			logging.error(e)
		
	def gitPush(self):
		print("push begins")
		try :
			repo.git.push()
			origin.push()
			print(config.pushConfirmationMsg)
		except Exception as e:
			logging.error(e)
	
	def excelWriter(self,gitURL,gitFileName,commitID):
		print("Excel Writer Begins")
		now = datetime.now()
		workbook = xlsxwriter.Workbook("GitHubUrl.xlsx")
		worksheet = workbook.add_worksheet()
		titleFormat = workbook.add_format({'bold': True, 'font_color': 'red'})
		titleFormat.set_align('center')
		worksheet.write('A1', 'File Name',titleFormat)
		worksheet.write('B1', 'GitHub File URL',titleFormat)
		worksheet.write('C1', 'COMMIT ID',titleFormat)
		worksheet.write('D1', 'File Upload Date',titleFormat)
		# worksheet.write('D1', 'Branch',titleFormat)
		
		for cellData in range(len(gitURL)):
			print(str(commitID[cellData]))
			exit()
			worksheet.write(cellData+1,0,gitFileName[cellData])
			worksheet.write(cellData+1,1,gitURL[cellData])
			worksheet.write(cellData+1,2,str(commitID[cellData]))
			worksheet.write(cellData+1,3,now.strftime("%d/%m/%Y %H:%M:%S"))
			# worksheet.write('D1', 'Branch',titleFormat)
		
		workbook.close()
		logging.info("Excel have been successfully created")
		print("Excel have been successfully created")

	def gitUrlFormation(self,filesCopied,gitFileName,commitID):
		gitURL = []
		gitDomain = config.gitUserCred['gitCloneUrl'].split(config.gitUserCred['gitHubRepository'])
		for file in filesCopied:
			docSplit = file.split(config.gitUserCred['gitHubRepository'])
			docName = docSplit[1].replace('\\', "/")
			fileURL = gitDomain[0] + config.gitUserCred['gitHubRepository'] + "/blob/master" + docName
			gitURL.append(fileURL)
		self.excelWriter(gitURL,gitFileName,commitID)
		
		
		
obj = gitPushPUML()		
obj.processStart()