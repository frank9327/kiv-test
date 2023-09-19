from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    pass



class MainWidget(Widget):
    pass


class WidgetLayoutApp(App):
    pass

# kv file must have exact same text the class above
WidgetLayoutApp().run()
