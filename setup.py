from setuptools import setup, find_packages

setup(
    name='document-header-editor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'docx',
        'pdf2docx',
        'pdf2image',
        'pytesseract',
        'Pillow'
    ],
)