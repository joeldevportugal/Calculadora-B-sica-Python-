from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        # Define o tamanho da janela
        Window.size = (290, 360)
        # Define a posição inicial da janela
        Window.left = 100
        Window.top = 100
        # Define a janela como não redimensionável
        Window.resizable = False

        self.title = 'Calculadora dev Joel ©'
        layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        self.result = TextInput(font_size=28, readonly=True, halign='right', multiline=False, size_hint=(1, 0.15))
        layout.add_widget(self.result)
        
        buttons = [
            ['%', 'C', '⌫', '/'],
            ['7', '8', '9', 'X'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', ',', '=', 'Autor']
        ]

        grid = GridLayout(cols=4, spacing=3, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                button = Button(text=label, font_size=22, size_hint=(1, 1))
                button.bind(on_release=self.on_button_click)
                grid.add_widget(button)
        
        layout.add_widget(grid)
        return layout

    def on_button_click(self, instance):
        if instance.text == 'C':
            self.result.text = ''
        elif instance.text == '⌫':
            self.result.text = self.result.text[:-1]
        elif instance.text == '=':
            try:
                expression = self.result.text.replace('X', '*').replace(',', '.')
                if '%' in expression:
                    while '%' in expression:
                        index = expression.index('%')
                        start = index - 1
                        while start >= 0 and (expression[start].isdigit() or expression[start] == '.'):
                            start -= 1
                        start += 1
                        number = float(expression[start:index]) / 100
                        expression = expression[:start] + str(number) + expression[index + 1:]
                self.result.text = str(round(eval(expression), 3)).replace('.', ',')
            except Exception:
                self.result.text = 'Erro'
        elif instance.text == 'Autor':
            self.show_author()
        else:
            self.result.text += instance.text

    def show_author(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Autor: Dev Joel 2024 ©\nPais: Portugal\nIdade: 32\n'))
        button = Button(text='Fechar', size_hint=(1, 0.25))
        content.add_widget(button)
        popup = Popup(title='Autor', content=content, size_hint=(0.75, 0.9))
        button.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    CalculatorApp().run()
