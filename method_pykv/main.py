import os
os.environ["KIVY_NO_ARGS"] = "1"
import kivy
import numpy as np
from kivymd.app import App
import cv2
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.properties import ObjectProperty

        
class MainApp(App):
    
    def build(self):
        return Builder.load_file('main.kv')


    def close_streaming(self, *args):
        App.get_running_app().stop()
        
    def streaming_video(self, *args):
        self.url = self.root.ids.txtaddress.text
        #url = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"
        self.capture = cv2.VideoCapture(self.url)
        while self.capture:
            Clock.schedule_interval(self.load_video, 0.25)
            break
    
    def load_video(self, *args):
        self.ret, self.frame = self.capture.read()
        if self.frame is not None:
            resize = cv2.resize(self.frame, (640,480))
            buffer = cv2.flip(resize,0).tostring()
            self.texture = Texture.create(size = (640,480), colorfmt = 'bgr')
            self.texture.blit_buffer(buffer, colorfmt = 'bgr', bufferfmt = 'ubyte')
            self.root.ids.image.texture = self.texture 
        else:
            pass

app = MainApp()
app.run()