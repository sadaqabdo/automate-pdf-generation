import os


for filename in os.listdir('.'):
    if filename.endswith('.pdf'): # only iterate through PDF files
        new_filename = filename.replace('&eacute;', 'é').replace('&ocirc;', 'ô')
        os.rename(os.path.join('.', filename), os.path.join('.', new_filename))
