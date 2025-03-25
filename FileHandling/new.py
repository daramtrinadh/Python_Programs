from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform

# For Android intents (will work when deployed on Android)
if platform == 'android':
    from jnius import autoclass

    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')


class CallApp(App):
    def build(self):
        # Set window size for desktop testing
        Window.size = (300, 500)

        # Create layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title
        title = Label(text="Phone Call App", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title)

        # Instructions
        instructions = Label(text="Enter a phone number below:", size_hint=(1, 0.1))
        layout.add_widget(instructions)

        # Text input for phone number
        self.phone_input = TextInput(hint_text="e.g., 1234567890", multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.phone_input)

        # Call button
        call_button = Button(text="Make Call", size_hint=(1, 0.2))
        call_button.bind(on_press=self.make_call)
        layout.add_widget(call_button)

        # Status label
        self.status = Label(text="", size_hint=(1, 0.3))
        layout.add_widget(self.status)

        return layout

    def make_call(self, instance):
        phone_number = self.phone_input.text.strip()

        if not phone_number:
            self.status.text = "Please enter a phone number!"
            return

        if not phone_number.isdigit():
            self.status.text = "Invalid number! Use digits only."
            return

        try:
            if platform == 'android':
                # Android-specific intent to make a call
                intent = Intent(Intent.ACTION_CALL)
                intent.setData(Uri.parse(f"tel:{phone_number}"))
                current_activity = PythonActivity.mActivity
                current_activity.startActivity(intent)
                self.status.text = f"Calling {phone_number}..."
            else:
                # For desktop testing, simulate the call
                self.status.text = f"Simulating call to {phone_number} (Desktop mode)"
        except Exception as e:
            self.status.text = f"Error: {str(e)}"


if __name__ == '__main__':
    CallApp().run()