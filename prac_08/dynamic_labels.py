from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_string('''
<BoxLayout>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        id: main
''')


class SimpleLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        self.title = "Simple Labels App"
        main_layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)
        return self.root


if __name__ == '__main__':
    SimpleLabelsApp().run()
