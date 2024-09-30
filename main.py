import random
import requests
import openai
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase


# Window.size = (360,800)

def get_current_weather(city):
    api_key = 'api_key'  # Replace with your actual API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        # Check for invalid city or other API errors
        if data.get('cod') == '404':
            return f"City '{city}' not found."
        elif data.get('cod') != 200:
            return f"Error fetching weather data: {data.get('message', 'Unknown error')}"

        # Safely access weather data using .get() to avoid KeyErrors
        weather = data.get('weather', [])
        if weather and len(weather) > 0:
            cloudiness = weather[0].get('description', 'No description available')
        else:
            return f"No weather information available for '{city}'."

        # Safely access other weather details
        temperature = data.get('main', {}).get('temp', 'N/A')
        feels_like = data.get('main', {}).get('feels_like', 'N/A')
        humidity = data.get('main', {}).get('humidity', 'N/A')
        wind_speed = data.get('wind', {}).get('speed', 'N/A')

        # Return formatted weather details
        return (f"\nThe weather in {city}:\n\n"
                f"Cloudiness: {cloudiness.capitalize()}\n"
                f"Temperature: {temperature}°C, feels like {feels_like}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s.")
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the weather: {e}"
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# print(get_current_weather("Jammu"))

def chat_Completion(text):
    openai.api_key = 'api_key'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text}"}],
        temperature=0.8
    )
    result = response['choices'][0]['message']['content']
    return result


# print(chat_Completion("Hello"))

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Sk-Modernist"
    font_size = 16


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Sk-Modernist"
    font_size = 16


class VirtuAI(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        self.icon = 'images/icon.png'
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("kv/Main.kv"))
        screen_manager.add_widget(Builder.load_file("kv/Chats.kv"))
        return screen_manager

    def hide_label(self, *args):
        self.root.ids.my_label.opacity = 0
        Clock.schedule_once(self.show_label, 3)

    def show_label(self, dt):
        self.root.ids.my_label.opacity = 1

    def response(self, *args):
        query = value
        greeting = ["hello", "hi", "hey"]
        greeting_response = ["Hello! How can I assist you today?", "Hey!, How may I help you?"]
        goodbye_response = ["Goodbye!, have a great day..", "GoodBye!"]
        goodbye = ["bye", "goodbye"]
        Thanks = ["thankyou", "thank you so much", "thanks alot"]
        thanks_response = ["Welcome!, Is there any anything else you want?",
                           "I am glad you are satisfied with the response.."]
        name = ["what is your name?", "who are you?", "your name?", "name"]
        name_response = ["I am VirtuAI developed by Akash Gupta and Utkarsh Gopal. You can ask anything who to....",
                         "I am VirtuAI, an AI chatbot model", "You can call me VirtuAI"]
        locations = ["Jammu","Srinagar","Delhi","Bangalore","Mumbai"]
        news = ['business','sports','technology','science','health','entertainment']
        if query.lower() in greeting:
            response = random.choice(greeting_response)
        elif query.lower() in goodbye:
            response = random.choice(goodbye_response)
        elif query.lower() in Thanks:
            response = random.choice(thanks_response)
        elif 'name'.lower() in query.lower():
            response = random.choice(name_response)
        elif query.lower() in name:
            response = random.choice(name_response)
        elif query.lower() in locations:
            response = random.choice
        elif 'weather'.lower() in query.lower():
            response = get_current_weather('Pune')
            # print(response)
        else:
            response = chat_Completion(query)
            # print(response)
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.40, halign="left"))
        """This method will generates response ."""

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .15
                halign = "center"
            elif len(value) < 11:
                size = .20
                halign = "center"
            elif len(value) < 16:
                size = .30
                halign = "center"
            elif len(value) < 21:
                size = .40
                halign = "center"
            elif len(value) < 26:
                size = .50
                halign = "center"
            else:
                size = .60
                halign = "center"
            screen_manager.get_screen('chats').chat_list.add_widget(
                Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""


if __name__ == '__main__':
    LabelBase.register(name="Sk-Modernist", fn_regular="fonts/Sk-Modernist-Regular.ttf")
    VirtuAI().run()
