# Setting Up a Python Virtual Environment

## 1. Install Virtualenv (if not installed)

```bash
    $ pip install virtualenv
```

## 2. Create a Virtual Environment

```bash
    $ virtualenv -p python3 venv
```

## 3. Activate the Virtual Environment

```bash
    $ source venv/bin/activate
```

## 4. Install Required Packages

```bash
    $ pip install -r requirements.txt
```

## 5. Verify Installation

```bash
    $ pip list
```

## 6. Once done, deactivate the Virtual Environment

```bash   
    $ deactivate
```

# Generating the PDF 

## i. Provide input and output files 

In generate_pdf.py, replace the values of input_html_file and output_pdf_file with the paths to your input HTML and provide a desirable name for your output PDF file, otherwise, leave defaults. 

## ii. Python Alias (optional)

```bash 
    $ alias py=python
``` 

## iii. Generate the PDF 

Run with alias: 

```bash 
    $ py generate_pdf.py
```

Without alias: 

```bash 
    $ python generate_pdf.py
```

## iv. Delete the generated PDF before repeating step (iii) on making changes to the input_html_file 



