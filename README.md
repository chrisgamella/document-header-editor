# Document Header Editor

The Document Header Editor is a versatile Python tool for adding headers to documents in various formats, including DOCX, PDF, and images. This library simplifies the process of customizing and adding headers to your documents programmatically.

## Features

- Add custom headers to DOCX documents.
- Insert headers into PDF files with ease.
- Overlay headers onto image files.
- Highly customizable header content, including text, images, and formatting options.
- Cross-platform support (Windows, macOS, and Linux).

## Installation

You can install the library using pip:

```bash
pip install document-header-editor
```


### Dependencies

- **docx**: A Python library for creating and manipulating Microsoft Word (.docx) files.
- **pdf2docx**: A Python library for converting PDF files to Microsoft Word (.docx) format.
- **pdf2image**: A Python library for converting PDF files to images.
- **pytesseract**: A Python wrapper for Google's Tesseract-OCR Engine, used for text recognition in images.
- **PIL (Pillow)**: The Python Imaging Library (Pillow), used for image processing tasks.

#### Installation

To install the project dependencies, you can use pip. Run the following command:


```bash
pip install -r requirements.txt
```



## Usage

Here's a basic example of how to use the library to add a header to a DOCX document:

```python
from document_header_library import HeaderGenerator

# Create a DOCXHeader instance with your document
header = HeaderGenerator()

# Load the file
header.load('input.docx')

# Customize the header content and formatting
header.set_text('My Document Header', font_size=14, bold=True)
header.set_alignment('center')

# Save the document with the new header
header.save('output.docx')
```





## Running Tests

To run the tests for this project, you'll need to set up your development environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/chrisgamella/document-header-editor.git

   cd document-header-editor

   ```

### Running with unittest

You can run the tests using `unittest` by running the following command:

```bash
python -m unittest discover -s tests
```