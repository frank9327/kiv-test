from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self,**kwarge):
        super().__init__(**kwarge)
        self.orientation = "lr-tb"
        b = Button(text="A",size_hint=(.5, .5))
    pass


class WidgetLayoutApp(App):
    pass


# kv file must have exact same text the class above
WidgetLayoutApp().run()
