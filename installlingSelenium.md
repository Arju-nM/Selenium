# Installing Selenium

At the time of installation of Selenium I was using [Anaconda](https://www.anaconda.com/) (open source distribution of Python and R) with
Python (version [3.7.1](https://www.python.org/downloads/release/python-371/)). 
So the installation processs given below works for this pair of versions and will most probably work for all future versions as well.

## Installing pip 
[pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) is a Pythion Package Manager which can be used to download and install
python packages.  
* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)  
* Search and locate the get-pip.py file on your computer
* Open Anaconda Prompt (search for Anaconda Prompt)
* Type and execute the single line code below
```python
python get-pip.py
```
Note: If you get the following error `can't open file 'get-pip.py': [Errno 2] No such file or directory` then try navigating to the
location of your get-pip.py file in the prompt ([command promt basics](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands))
and then executing the code or add the location of the file as `path` in environment variables ([how to set path](https://www.computerhope.com/issues/ch000549.htm)). 

## Installing Selenium Package

* Open Anaconda Prompt (search for Anaconda Prompt)  
* Type and execute the single line code below  
```python
pip install selenium
```  
Note: You will know that the download and installation of your package is complete if the prompt window shows something along the lines of
**Successfully installed ...**

## Installing Selenium Webdriver

* Download the webdriver according to the browser of you choice, links are provided below:
|Browser  |
|---------|
|Chrome   |
|Edge     |
|Firefox
|Safari
