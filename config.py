#!/usr/bin/env python
import os

gitUserCred = {'userName' : 'ashokkumarsoliyappan',
		'userEmail' : 'sashoksee@gmail.com',
		'userPassword' : 'Adventure160894',
		'gitCloneUrl' : 'https://github.com/ashokkumarsoliyappan/gitTest.git',
		'gitHubRepository' : 'gitTest'
		}

localGitRepository = {'gitLocalConfig' : R'C:\Users\z028605\AppData\Local\Programs\Python\Python37-32\.git',
		'gitLocalRepository' : ''}
		
LOGFIleNAME= "autogitlog"

userExcelPath = os.environ['USERPROFILE'] + "\Desktop\gitUrl.xlsx"
repoClonnedExist = "The Repository already exists"
repoClonnedSuccessMsg = "Repository clonned now"
pushConfirmationMsg = "Latest changes and files have been commited to the GitHub remote Repository"
keyboardInterruptlog = "You have interrupted the program through keyboard"
