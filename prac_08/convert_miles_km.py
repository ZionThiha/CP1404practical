from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class Converter(BoxLayout):

    kilometers = StringProperty('0.0')

    def convert(self, miles):
        try:

            self.kilometers = str(float(miles) * MILES_TO_KM)
        except ValueError:

            self.kilometers = '0.0'

    def increment(self, value):
        try:
            miles = float(self.ids.input_miles.text) + value
            self.ids.input_miles.text = str(miles)
            self.convert(miles)
        except ValueError:
            start_value = value if value != 0 else 1
            self.ids.input_miles.text = str(start_value)
            self.convert(start_value)

class ConvertApp(App):
    def build(self):
        return Converter()

if __name__ == '__main__':
    ConvertApp().run()
