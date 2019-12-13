#!/usr/bin/env python
import os

# config for PUML Automation
gitUserCred = {'userName' : 'github account name',
		'userEmail' : 'email',
		'userPassword' : 'password',
		'gitCloneUrl' : 'git hub repository url',
		'gitHubRepository' : 'repostiory name'
		}

localGitRepository = {'gitLocalConfig' : R'local git .git path',
		'gitLocalRepository' : ''}
		
userExcelPath = os.environ['USERPROFILE'] + "\Desktop\gitUrl.xlsx"
repoClonnedExist = "The Repository already exists"
repoClonnedSuccessMsg = "Repository clonned now"
pushConfirmationMsg = "Latest changes and files have been commited to the GitHub remote Repository"
keyboardInterruptlog = "You have interrupted the program through keyboard"
LOGFIleNAME= "autogitlog"

		

# config for file  upload to Azure Blob storage
azureBlobConnect = {'accountName' : 'blob storage account name',
		'accountKey' : 'blob storage account key',
		'connectionStr' : 'blob storage connection string',
		'containerName' : "blob storage container name"
		}
mailConfig = { 'mailSubject' : 'mail subject',
		'mailTo'	: "TO mail id",
		'mailCC'	: "CC Mail ID",
		'mailBody'	: "Hi Team <p>Good day.</p> <p>Please find the mail</p> <p>Regards, <br>team</p>"
}
csvLocalPath = R"csv file local Path"
BlobLogFileName = "Log file name" 

 # to add mulitple email use semi-colon ";" as the seperator between two mail
