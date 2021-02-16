Invoice generator for Lirik (twitch.tv/lirik) by l8sek

1. install Python (newest one will do), BE SURE TO CHECK "include in PATH" OR SOMETHING LIKE THAT DURING INSTALLATION
2. in order to use Imgur upload API create a new application in Imgur Account Settings, then copy Client ID and paste it into imgur_client_id
3. launch command prompt in the folder containing invoice.py
4. type "python invoice.py"
5. input the name of invoicee
6. wait and copy the link to the image

Technicalities:
Script reads "form.docx" which you can modify, just don't change the three lines that are modified by the program. It modifies the contents, saves as a new .docx, converts it into .pdf, then into .jpg, and finally uploads to imgur through their API.