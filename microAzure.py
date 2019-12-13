from azure.storage.blob import BlockBlobService, PublicAccess
from sys import exit
import os, uuid, sys
import glob
import logging
import config
import win32com.client

class AzureBlobFileUpload():

	errorLogFormat = "%(asctime)s:::%(filename)s:::%(message)s"
	logFormat = "%(asctime)s:::%(filename)s:::%(message)s"
	logging.basicConfig(filename=config.BlobLogFileName,level=logging.INFO, format = logFormat)
	logging.basicConfig(filename=config.BlobLogFileName,level=logging.error, format = errorLogFormat)
		
	def processStart(self):
		accountName = config.azureBlobConnect['accountName']
		accountKey = config.azureBlobConnect['accountKey']
		connectionStr = config.azureBlobConnect['connectionStr']
		containerName = config.azureBlobConnect['containerName']
		self.azureConnection(accountName,accountKey,connectionStr,containerName)
		logging.info("================>Process Ended<================")

	def azureConnection(self,accountName,accountKey,connectionStr,containerName):
		try:
			logging.info("================>ProcessStarted<================")
			print(containerName)
			global blob_service_client
			blob_service_client = BlockBlobService(account_name=accountName, account_key=accountKey)
			# blob_service_client.set_container_acl(containerName, public_access=PublicAccess.Container)
			self.listBlob(containerName) #to list the blobs in the container
			self.fileUploadBlob(containerName) # to upload the files
		except Exception as e:
			print(e)
	
	def listBlob(self,containerName):
		logging.info("List the blob")
		try:
			generator = blob_service_client.list_blobs(containerName)
			for blob in generator:
				print("\t Blob name: " + blob.name)
		except Exception as e:
			logging.error(e)
		
	def fileUploadBlob(self,containerName):
		blobFiles = []
		print("Upload")
		definedFileFormat = "**/*.csv"
		csvLocalFolderPath = config.csvLocalPath
		blobFiles = [f for f in glob.glob(csvLocalFolderPath + definedFileFormat, recursive=False)]
		logging.info("Csv files have been filtered and Selected from the local Path")
		for blob in blobFiles:
			try:
				fullBlobPath,fileName = os.path.split(blob)
				blob_service_client.create_blob_from_path(containerName, fileName, blob)
				logging.info("{}=> {}".format(fileName,fullBlobPath))
			except Exception as e:
				logging.error(e)
		logging.info("All the Files have been uploaded to Azure blob storage")
		self.mailForward()
		
	def mailForward(self):
		mailTrig = win32com.client.Dispatch("Outlook.Application")

		Msg = mailTrig.CreateItem(0)
		Msg.Importance = 0
		Msg.Subject = config.mailConfig['mailSubject']
		Msg.HTMLBody = config.mailConfig['mailBody']

		Msg.To = config.mailConfig['mailTo']
		Msg.CC = config.mailConfig['mailCC']
		Msg.Send()
		logging.info("Successfuly Mail Haven been sent")
			
obj = AzureBlobFileUpload()
obj.processStart()