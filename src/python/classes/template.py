import pathlib
import os

# TEMPLATE_DIR = "../template"

class Template:
    def __init__(self, name="basic", dir=None, file=None, placeholder="{main_content}"):
        template_dir =  f"{os.path.dirname(os.path.realpath(__file__))}/../../template"

        self.name = name or "basic"
        self.dir = dir or f"{template_dir}/{self.name}"
        self.file = file or f"{template_dir}/{self.name}/index.html"
        self.placeholder = placeholder
        self.content = ""

        if self.file:
            with open(self.file, 'r') as tf:
                self.content = tf.read()

    def page(self, data):
        return self.content.replace(self.placeholder, data)


    
