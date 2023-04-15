# Automate Generation of Documents

This repository contains the source code for the [Automate Generation of Documents], instead of writing them manually, and each time we change the name of the destinataire, we automatically change the name of the destinataire in the document, by using a template.

Note: This is a just example of applying it to job application letters, but you can use it for any document you want to generate.

We utilise:
- the [Jinja2] template engine to generate the documents
- PDFKit to convert the HTML to PDF
- [wordtohtml](https://wordtohtml.net/) to convert the Word document to HTML

## Installation

```bash
pip install jinja2 pdfkit
```

and install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) for your operating system.

## Usage

We utilise the [Jinja2] template engine to generate the documents. The template is in the `template.html` file.
You can change the template to your needs, and add the variables you want to use in this format : {{variable}}.
also you can add the variables you want to use in the `generate.py` file in the `data` dictionary.

```bash
python generate.py
```
