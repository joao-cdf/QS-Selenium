# QS-Selenium

- João Ferreira m10642
- Luís David m10698

Link to the report - https://www.overleaf.com/project/5fc762d627c45a17deb3fd37

A Testing Application to use with [Smart Home Assistant](https://github.com/joaoferreira7991/smart_home_assistant) in order to explore the Selenium framework. 

## Setup 

The code was developed using Python 3.9. Go [here](https://www.python.org/downloads/) to install it on windows.

After installing, clone this repository on your computer.

```bash
git clone https://github.com/joaoferreira7991/QS-Selenium.git
```

Now enter the directory and create a virtual environment, so that we can have a clean python environment for the application.

```bash
cd QS-Selenium
python -m venv virtual
```

After the environment is created you need to access the virtual environment, make sure that you are inside the environment by checking for a (virtual) header on your prompt.

```bash
.\virtual\Scripts\activate
```

Now you need to install the selenium module through pip. Again check that the (virtual) header is on your prompt.

```bash
python -m pip install --upgrade
python -m pip install selenium
```

And voila! For the final step you run the application with 

```bash
python app/main.py
```

Remember, in order to run main.py you need to be inside the virtual environment where selenium is installed. To exit the environment use this.

```bash
deactivate
```
