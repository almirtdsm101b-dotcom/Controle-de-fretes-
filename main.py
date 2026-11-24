from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ControleFreteApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Controle de Fretes"))
        layout.add_widget(Button(text="Testar"))
        return layout


if __name__ == "__main__":
    ControleFreteApp().run()
