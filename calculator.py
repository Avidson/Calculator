from kivy.app import App 
from kivy.uix.layout import Layout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 


class Calculator(App):

    def on_solution(self, instance):
        text = self.solution.text 
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution 


    def on_button_press(self, instance):
            current = self.solution.text
            button_text = instance.text 

            if button_text == "C":
                #clear the solution widget
                self.solution.text = ""
            else:
                if current and (self.last_was_operator and button_text in self.operators):
                    return button_text

                elif current == "" and button_text in self.operators:
                    # First character cannot be an operator
                    return 
                else:
                    new_text = current + button_text 
                    self.solution.text = new_text 
            self.last_button = button_text 
            self.last_was_operator = self.last_button in self.operators 

            

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None 
        self.last_button = None 
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55,
            
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x' : .5, 'center_y' : .5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text = "=", pos_hint={'center_x': .5, 'center_y': .5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

        

if __name__ == '__main__' :
    Calculator().run()