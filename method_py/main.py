import os
os.environ["KIVY_NO_ARGS"] = "1"
import kivy
import numpy as np
from kivymd.app import App
import cv2
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.lang import builder
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
        
class MainApp(App):
    
    def build(self):
        main_layout = BoxLayout(orientation = 'vertical')
        top_layout = BoxLayout(orientation = 'horizontal')

        self.image = Image()
        top_layout.add_widget(self.image) # image added to top layout

        grid_layout = GridLayout()
        grid_layout.rows = 1
        grid_layout.cols = 3
        grid_layout.size_hint_y = 0.06
        

        self.text_input = TextInput(hint_text='Enter IP address or RTSP stream address', size_hint_x = 4)
        #self.text_input.add_widget(Label(text="Ip or Port"))
        
        
        grid_layout.add_widget(self.text_input)

        self.satrt_button = Button(text =  "Start ",
                background_color = [0, 1, 0, 1],
                font_size =  30) 
        self.satrt_button.bind(on_press = self.streaming_video)

        self.stop_button = Button(text =  "Close",
                background_color = [1, 0, 0, 1],
                font_size =  30)
        self.stop_button.bind(on_press = self.close_streaming)
        grid_layout.add_widget(self.satrt_button)
        grid_layout.add_widget(self.stop_button)

        
        main_layout.add_widget(top_layout)
        main_layout.add_widget(grid_layout)
        
        return main_layout

    def close_streaming(self, *args):
        App.get_running_app().stop()
        
            


    def streaming_video(self, *args):
        url = self.text_input.text
        #url = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"
        self.capture = cv2.VideoCapture(url)
        while self.capture:
            Clock.schedule_interval(self.load_video, 0.25)
            break
    
    def load_video(self, *args):
        ret, frame = self.capture.read()
        if frame is not None:
            resize = cv2.resize(frame, (640,480))
            buffer = cv2.flip(resize,0).tostring()
            texture = Texture.create(size = (640,480), colorfmt = 'bgr')
            texture.blit_buffer(buffer, colorfmt = 'bgr', bufferfmt = 'ubyte')
            self.image.texture = texture 
        else:
            pass



app = MainApp()
app.run()
