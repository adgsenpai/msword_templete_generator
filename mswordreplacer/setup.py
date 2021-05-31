from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mswordreplacerdict',
  version='0.0.1',
  description='python program to convert data dictionaries to replace fields in word document',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ashlin Darius Govindasamy',
  author_email='adgrules@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='msword', 
  packages=find_packages(),
  install_requires=['python-docx'] 
)