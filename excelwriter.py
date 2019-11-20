# import xlsxwriter

# workbook = xlsxwriter.Workbook("Text.xlsx")
# worksheet = workbook.add_worksheet()

# #header format
# boldFormat = workbook.add_format({'bold': True, 'font_color': 'red'})
# boldFormat.set_align('center')
# #header declarartion
# worksheet.write('A1', 'File Name',boldFormat)
# worksheet.write('B1', 'GitHub File URL',boldFormat)

# for data in range(len(gitUrl)):
	# worksheet.write(data+1,0,gitUrl[fileName])
	# worksheet.write(data+1,1,values[gitUrl])
# workbook.close()
import subprocess
label = subprocess.check_output(["git", "log -1"]).strip()
print(label)