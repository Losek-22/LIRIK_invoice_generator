from docx import Document
from datetime import date
import datetime
from docx2pdf import convert
from pdf2image import convert_from_path
import pyimgur
import os


while True:
	try:
		# custom data going into the form
		input_name = input("Input the person's name:\n")
		today = date.today()
		tomorrow = today + datetime.timedelta(days=1)

		# read template, modify it, save it as .docx
		document = Document('form.docx')
		for paragraph in document.paragraphs:
			if 'NAME2' in paragraph.text:
				paragraph.text = f'Tenant name: {input_name}'
			if 'INVOICE_DATE' in paragraph.text:
				paragraph.text = f'Invoice date: {today}'
			if 'DUE_DATE' in paragraph.text:
				paragraph.text = f'Due date: {tomorrow}'
		document.save('temp.docx')

		# convert .docx to .pdf
		convert('temp.docx')

		# convert .pdf to .jpeg
		pages = convert_from_path('temp.pdf', 500, poppler_path=r'poppler\Library\bin')
		for page in pages:
			page.save('temp.jpg', 'JPEG')

		# upload to imgur
		with open('imgur_client_id.txt', 'r') as f:												# read client_id for imgur
			CLIENT_ID = f.readlines()[0]
		PATH = "temp.jpg"
		im = pyimgur.Imgur(CLIENT_ID)
		uploaded_image = im.upload_image(PATH, title=f"Invoice for {input_name}")

		print(f'Link to the uploaded invoice:\n {uploaded_image.link}\n')

	except Exception as e:
		print(f'Exception occured:\n{e}\n')
