from setuptools import setup
from telebase import version
from telebase import autor
from telebase import email


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

setup(
    name='telebase',
    version=version,
    description='Telebase é um projeto de código aberto que visa a criação de um sistema de gerenciamento de dados '
                'json para o Telegram.',
    long_description=readme,
    long_description_content_type='text/markdown',

    url='https://github.com/marcellobatiista/Telebase',
    author=autor,
    author_email=email,

    keywords='telegram chat messenger api db json database crud library python',
    python_requires='>=3.7',
    packages=['telebase'],
    install_requires=requires
)

