from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

class MainApp(MDApp):
    title = "Sims Scenarios"


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"


        player = VideoPlayer(source="videoapp.mov")

        player.state = 'play'

        return player

MainApp().run()