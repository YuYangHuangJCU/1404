"""
CP1404 Week 11 Workshop - GUI program to convert mile_ to kilometres
Lindsay Ward, IT@JCU
05/10/2015
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Yuyang Huang'

KM = 1.60934


class mile_Converter(App):
    """ mile_Converter is a Kivy App for converting mile_ to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert mile_ to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_mile()
        result = value * KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        value = self.get_mile() + change
        self.root.ids.input_mile_.text = str(value)
        self.handle_calculate()

    def get_mile(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_mile_.text)
            return value
        except ValueError:
            return 0


mile_Converter().run()
