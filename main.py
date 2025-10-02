import torch
from TTS.api import TTS
import gradio as gr 

device ="cuda" if torch.cuda.is_available() else "cpu"
print("enter the text you want to transform:")
text = str(input())

def generate_audio(text):
    tts = TTS(model_name='tts_models/en/jenny/jenny').to(device)
    tts.tts_to_file(text=text, file_path="outputs/output.wav")
    return "outputs/output.wav"

demo = gr.Interface(
    fn=generate_audio,
     inputs=[gr.Text(label="Text"),],
     outputs=[gr.Audio(label="Audio"),],
)


demo.launch()
