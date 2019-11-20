import xlsxwriter

workbook = xlsxwriter.Workbook("GitHubUrl.xlsx")
worksheet = workbook.add_worksheet()

#header format
titleFormat = workbook.add_format({'bold': True, 'font_color': 'red'})
titleFormat.set_align('center')
#header declarartion
worksheet.write('A1', 'File Name',titleFormat)
worksheet.write('B1', 'GitHub File URL',titleFormat)

# for data in range(len(gitUrl)):
	# worksheet.write(data+1,0,gitUrl[fileName])
	# worksheet.write(data+1,1,values[gitUrl])
workbook.close()

# workbook = xlsxwriter.Workbook("GitHubUrl.xlsx")
# worksheet = workbook.add_worksheet()


# worksheet.write('A1', 'File Name',titleFormat)
# worksheet.write('B1', 'GitHub File URL',titleFormat)
# worksheet.write('C1', 'File Uploaded Date',titleFormat)
