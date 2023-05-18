# ChatBot-Jarvis
It is my first project build on python using python kivymd library.

You will need to create a virtual environment, before running the 'chatbot.py' file. 
I have used python 3.7.4 for this project.
By using the following commands in any terminal in Windows Machine (powershell is recommended):
    
    pip install virtualenv venv
    .\venv\Scripts\activate.ps1 
    
    (This command will create and activate the virtual environment named 'venv' in powershell.)
  
Now, some necessary modules are required to install in order to run the code safely, using the pip command in the same environment.
   
    pip install requests
    pip install kivy
    pip install kivymd
    pip install newsapi-python
    pip install termcolor
    
After installing these modules, you must get your API keys from 
    https://openweathermap.org/ : for weather API and replace it with the text 'API_KEY' in weather.py file.
    https://newsapi.org/        : for news API and replace it with the text 'YOUR_API_KEY' in news.py file.
Now, you're are all set to use this chatbot. 

By running the chatbot.py file in the enironment. 
