import gradio as gr
import PIL

class FlanT5:
    def __init__(self):
        self.space = gr.Interface.load("spaces/osanseviero/i-like-flan") 

    def __call__(self, text):
        return self.space(text)[0]

class MagicPrompt:
    def __init__(self):
        self.space = gr.Interface.load("spaces/Gustavosta/MagicPrompt-Stable-Diffusion") 

    def __call__(self, text):
        return self.space(text)
