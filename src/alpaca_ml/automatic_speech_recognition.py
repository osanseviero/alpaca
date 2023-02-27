import gradio as gr

class Whisper:
    def __init__(self):
        self.space = gr.Interface.load("spaces/openai/whisper") 

    def __call__(self, audio_path):
        return self.space(audio_path)[0]

class Wav2vec2:
    def __init__(self):
        self.space = gr.Interface.load("spaces/DrishtiSharma/ASR_using_Wav2Vec2") 

    def __call__(self, audio_path):
        return self.space(audio_path)