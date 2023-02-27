import gradio as gr
import PIL

class AnimeGan:
    def __init__(self):
        self.space = gr.Interface.load("spaces/akhaliq/AnimeGANv2") 

    def __call__(self, img_path):
        res_img = self.space(img_path, "version 2 (🔺 robustness,🔻 stylization)")
        return PIL.Image.open(res_img)

class ArcaneGan:
    def __init__(self):
        self.space = gr.Interface.load("spaces/akhaliq/ArcaneGAN") 

    def __call__(self, img_path):
        res_img = self.space(img_path, "version 0.4")
        return PIL.Image.open(res_img)

class GFPGAN:
    def __init__(self):
        self.space = gr.Interface.load("spaces/Xintao/GFPGAN") 

    def __call__(self, img_path):
        res_img = self.space(img_path,  "v1.4", 2)[0]
        return PIL.Image.open(res_img)