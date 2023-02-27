import gradio as gr

class BlipCaptioner:
    def __init__(self):
        self.space = gr.Interface.load("spaces/Salesforce/BLIP") 

    def __call__(self, img_path):
        return self.space(img_path, "Image Captioning", None, "Nucleus sampling")

class BlipQuestionAnswerer:
    def __init__(self):
        self.space = gr.Interface.load("spaces/Salesforce/BLIP") 

    def __call__(self, img_path, question):
        return self.space(img_path, "Visual Question Answering", question, "Nucleus sampling")