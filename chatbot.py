import random
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from news import get_news
from weather import get_current_weather
from openAPI import chat_Completion


# Window.size = (360,800)
class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Sk-Modernist-Regular"
    font_size = 16


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Sk-Modernist-Regular"
    font_size = 16


class ChatBot(MDApp):
    def change_screen(self, name):
        screen_manager.current = name
        """This method will change screen."""

    def build(self):
        global screen_manager
        self.icon = 'icon.png'
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        """This method links python code with kv files."""
        return screen_manager

    def response(self, *args):
        query = value
        greeting = ["hello", "hi", "hey"]
        greeting_response = ["Hello! How can I assist you today?", "Hey!, How may I help you?"]
        goodbye_response = ["Goodbye!, have a great day..", "GoodBye!"]
        goodbye = ["bye", "goodbye"]
        Thanks = ["thankyou", "thank you so much", "thanks alot"]
        thanks_response = ["Welcome!, Is there any anything else you want?",
                           "I am glad you are satisfied with the response.."]
        # locations = ["Jammu","Srinagar","Delhi","Bangalore","Mumbai"]
        if query.lower() in greeting:
            response = random.choice(greeting_response)
        elif query.lower() in goodbye:
            response = random.choice(goodbye_response)
        elif query.lower() in Thanks:
            response = random.choice(thanks_response)
        elif 'business'.lower() in query.lower():
            response = get_news("business")
        elif 'sports'.lower() in query.lower():
            response = get_news("sports")
        elif 'tech'.lower() in query.lower():
            response = get_news("technology")
        elif 'science'.lower() in query.lower():
            response = get_news("science")
        elif 'tech'.lower() in query.lower():
            response = get_news("technology")
        elif 'health'.lower() in query.lower():
            response = get_news("health")
        elif 'entertainment'.lower() in query.lower():
            response = get_news("entertainment")
        elif 'weather'.lower() in query.lower():
            response = get_current_weather("Jammu")
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
    LabelBase.register(name="Sk-Modernist-Regular", fn_regular="Sk-Modernist-Regular.ttf",
                       fn_bold="Sk-Modernist-Bold.ttf")
    ChatBot().run()
