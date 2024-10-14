from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class ConverterApp(App):
    def build(self):
        #  BoxLayout for overall layout
        self.layout = BoxLayout(orientation='vertical')

        # Background image covering the entire window
        with self.layout.canvas.before:
            self.background = Image(source='amazing spiderman.jpg', allow_stretch=True, keep_ratio=False)
            self.layout.bind(size=self.update_background)

        #  GridLayout for the input and output section
        grid = GridLayout(cols=1, padding=20, spacing=15, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Input field 
        self.input_field = TextInput(hint_text='Enter value', size_hint=(1, 0.1), font_size=16)
        grid.add_widget(self.input_field)

        # Conversion Mode Selectors 
        self.from_base_spinner = Spinner(
            text='Decimal',
            values=('Decimal', 'Binary', 'Octal', 'Hexadecimal'),
            size_hint=(1, 0.1),
            font_size=14
        )
        grid.add_widget(self.from_base_spinner)

        self.to_base_spinner = Spinner(
            text='Decimal',
            values=('Decimal', 'Binary', 'Octal', 'Hexadecimal'),
            size_hint=(1, 0.1),
            font_size=14
        )
        grid.add_widget(self.to_base_spinner)

        # Convert button 
        self.convert_button = Button(text='Convert', size_hint=(1, 0.1), font_size=16)
        self.convert_button.bind(on_press=self.convert)
        grid.add_widget(self.convert_button)

        # Output label with a fancy design 
        self.output_label = Label(size_hint=(1, 0.1), 
                                  text='Converted Value:', 
                                  font_size='18sp', 
                                  halign='center', 
                                  valign='middle',
                                  color=(1, 1, 1, 1))
        self.output_label.bind(size=self.output_label.setter('text_size'))

        #  background for the output label
        with self.output_label.canvas.before:
            Color(0, 0, 0, 0.5)  # Set the color to black with transparency
            self.rect = Rectangle(size=self.output_label.size, pos=self.output_label.pos)

        self.output_label.bind(size=self.update_rect, pos=self.update_rect)
        grid.add_widget(self.output_label)

        # Clear button 
        self.clear_button = Button(text='Clear', size_hint=(1, 0.1), font_size=16)
        self.clear_button.bind(on_press=self.clear_inputs)
        grid.add_widget(self.clear_button)

        # Add the grid to the main layout
        self.layout.add_widget(grid)

        return self.layout

    def update_background(self, instance, value):
        #  background size and position
        self.background.size = instance.size
        self.background.pos = instance.pos

    def update_rect(self, instance, value):
        #  the rectangle size and position
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def convert(self, instance):
        input_value = self.input_field.text

        # Get the selected conversion mode
        from_base = self.from_base_spinner.text
        to_base = self.to_base_spinner.text

        # Conversion logic
        try:
            if from_base == 'Decimal':
                decimal_value = int(input_value)
            elif from_base == 'Binary':
                decimal_value = int(input_value, 2)
            elif from_base == 'Octal':
                decimal_value = int(input_value, 8)
            elif from_base == 'Hexadecimal':
                decimal_value = int(input_value, 16)

            # Convert to the target base
            if to_base == 'Decimal':
                converted_value = str(decimal_value)
            elif to_base == 'Binary':
                converted_value = bin(decimal_value)[2:]  # Skip the '0b' prefix
            elif to_base == 'Octal':
                converted_value = oct(decimal_value)[2:]   # Skip the '0o' prefix
            elif to_base == 'Hexadecimal':
                converted_value = hex(decimal_value)[2:].upper()  # Skip '0x'

            self.output_label.text = f"Converted Value: {converted_value}"
        except ValueError:
            self.output_label.text = "Invalid Input!"

    def clear_inputs(self, instance):
        self.input_field.text = ''
        self.output_label.text = 'Converted Value:'

if __name__ == '__main__':
    ConverterApp().run()
