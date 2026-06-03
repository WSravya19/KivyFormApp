from kivy.app import App
from kivy.lang import Builder
import json

class MyApp(App):

    def build(self):
        return Builder.load_file("my.kv") 

    def save_data(self):

        name = self.root.ids.name.text
        email = self.root.ids.email.text
        mobile = self.root.ids.mobile.text

        data = {
            "name": name,
            "email": email,
            "mobile": mobile
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data Saved Successfully")

MyApp().run()