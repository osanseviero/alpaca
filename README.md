# Alpaca ML

Alpaca is a minimalistic, proof-of-concept library for simple inference of models using available APIs offered by Gradio through their [Spaces](https://huggingface.co/spaces) integration. The library is not focused on production-level APIs but rather simple proof of concepts and chaining of models.

The library is focused on simplicity rather than customizability and generalization. The current library allows for the following tasks.

## Image to Image

The module has three utilities for image stylization

* [AnimeGan](https://huggingface.co/spaces/akhaliq/AnimeGANv2) for face portraits
* [ArcaneGan](https://huggingface.co/spaces/akhaliq/ArcaneGAN) for Arcane style face stylization
* [GFPGAN](https://huggingface.co/spaces/Xintao/GFPGAN) for restoration

```python
from alpaca_ml import ArcaneGan

model = ArcaneGan()
model("bill.png")
```

## Text Generation

The module has two utilities for text generation

* [FlanT5 XXL](https://huggingface.co/spaces/osanseviero/i-like-flan) for high-quality generation
* [MagicPrompt](https://huggingface.co/spaces/Gustavosta/MagicPrompt-Stable-Diffusion) for prompt generation

```python
from alpaca_ml import FlanT5

generator = FlanT5()
generator("Q: Can Barack Obama have a conversation with George Washington? Give the rationale before answering.")
# 'George Washington died in 1799. Barack Obama was born in 1961. The answer: no.'
```

## Automatic Speech Recognition

Given an audio file, the model can transcribe it into text. The module contains two utilities:

* Whisper, considered one of the best open source models for the task
* Wav2vec2

```python
from alpaca_ml import Whisper

whisper = Whisper()
whisper("sample.flac")
# "going along slushy country roads and speaking to damp audiences in drafty school rooms day after day for a fortnight. He'll have to put in an appearance at some place of worship on Sunday morning, and he can come to us immediately afterwards."
```

## Image to text

There are two utilities based on [BLIP](https://huggingface.co/spaces/Salesforce/BLIP) from Salesforce:

* Image captioning: describes the image
* Visual question answering: based on an image and a question, get the answer to them

```python
from alpaca_ml import BlipCaptioner

captioner = BlipCaptioner()
captioner("bill.png")
# 'caption: bill gates wearing glasses and a sweater'
```

And here is Visual Question Answering

```python
from alpaca_ml import BlipQuestionAnswerer

answerer = BlipQuestionAnswerer()
answerer("bill.png", "Does the person in the picture have glasses?")
# 'answer: yes'
```

## Creative use cases

1. 