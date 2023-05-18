from symbol import parameters
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty 
from kivy.core.text import LabelBase
from intents import intents
import random
from news import get_news
from weather import get_current_weather

Window.size = (350,550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x =  NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 16

class Response(MDLabel):
    text = StringProperty()
    size_hint_x =  NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 16

class ChatBot(MDApp):
    def change_screen(self, name):
        screen_manager.current = name
        """This method will change screen."""

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        """This method links python code with kv files."""
        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"
            """This method sets bot name."""

    def response(self, *args):
        user_input = value
        matched_intent = None
        for intent in intents:
            for pattern in intent['patterns']:
                if user_input.lower() == pattern:
                    matched_intent = intent
                    break
            if matched_intent:
                break
        if matched_intent:
            if 'greeting' in matched_intent['name']:
                response = random.choice(matched_intent['responses'])+"\n"
                #print(response)
                news_intents = []
                for intent in intents:
                    if 'news' in intent['name']:
                        news_intents.append(intent['name'])
                news_categories = "\n- ".join([intent.replace('_news', '') for intent in news_intents])
                response += f"\nHere are the available news categories:\n- {news_categories}"
                #print(response)
            elif 'business_news' in matched_intent['name']:
                articles = get_news("business")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'entertainment_news' in matched_intent['name']:
                articles = get_news("entertainment")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'sports_news' in matched_intent['name']:
                articles = get_news("sports")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'science_news' in matched_intent['name']:
                articles = get_news("science")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'technology_news' in matched_intent['name']:
                articles = get_news("technology")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'sports_news' in matched_intent['name']:
                articles = get_news("sports")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif 'health_news' in matched_intent['name']:
                articles = get_news("health")
                if articles:
                    response = random.choice(matched_intent['responses'])+ articles
                    #print(response)
            elif  'weather' in matched_intent['name']:
                    location = "Jammu"
                    weather= get_current_weather(location)
                    if weather:
                        response = random.choice(matched_intent['responses']) + weather
            else:
                response = random.choice(matched_intent['responses'])
        else:
            response = "I'm sorry, I don't understand."
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response,size_hint_x = .80))
        """This method will generates response ."""

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) <6:
                size = .22
                halign = "center"
            elif len(value) <11:
                size = .32
                halign = "center"
            elif len(value) <16:
                size = .45
                halign = "center"
            elif len(value) <21:
                size = .58
                halign = "center"
            elif len(value) <26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value,size_hint_x=size, halign = "halign"))
            Clock.schedule_once(self.response,2)
            screen_manager.get_screen('chats').text_input.text = ""

if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
