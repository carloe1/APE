#! PYTHON3
## DataSheet.py - Read data sheet and create an index

import xlrd, sys

class DataSheet:

	def __init__(self, fileName):

		## List containing a dictionaries representing each row 
		self.data = []

		## Open given file name
		workbook 	= xlrd.open_workbook(fileName)
		workbook 	= xlrd.open_workbook(fileName, on_demand = True)
		worksheet 	= workbook.sheet_by_index(0)

		## The row where we stock the name of the column
		self.columns = [] 
		for col in range(worksheet.ncols):
		    self.columns.append( worksheet.cell_value(0,col) )
		
		## Append Rows to data variable
		for row in range(1, worksheet.nrows):
		    elm = dict()
		    for col in range(worksheet.ncols):
		        elm[self.columns[col]] = worksheet.cell_value(row,col)
		    self.data.append(elm)


	def getData(self):
		return self.data

	def __str__(self):
		DataSheetValues = ""
		for row in self.data:
			for col in row:
				DataSheetValues += col + ":" + row[col] + " | "
			DataSheetValues += "\n"

		return DataSheetValues

	def __repr(self):
		DataSheetValues = ""
		for row in self.data:
			for col in row:
				DataSheetValues += col + ":" + row[col] + " | "
			DataSheetValues += "\n"

		return DataSheetValues