import gradio as gr
import os
from app.text2midi.model.transformer_model import test_generate
input_text = gr.Textbox(lines=2, label="Prompt")
output_audio = gr.Audio(label="Generated Music", type="filepath")
output_midi = gr.File(label="Download MIDI File")
temperature = gr.Slider(minimum=0.9, maximum=1.1, value=1.0, step=0.01, label="Temperature", interactive=True)
max_length = gr.Number(value=1500, label="Max Length", minimum=500, maximum=2000, step=100)
app = gr.Interface(
    fn=test_generate,
    inputs=[input_text, temperature, max_length],
    outputs=[output_midi],
    description=description_text,
    allow_flagging=False,
    examples=[
        ["A haunting electronic ambient piece that evokes a sense of darkness and space, perfect for a film soundtrack. The string ensemble, trumpet, piano, timpani, and synth pad weave together to create a meditative atmosphere. Set in F minor with a 4/4 time signature, the song progresses at an Andante tempo, with the chords F, Fdim, and F/C recurring throughout."],
        ["A slow and emotional classical piece, likely used in a film soundtrack, featuring a church organ as the sole instrument. Written in the key of Eb major with a 3/4 time signature, it evokes a sense of drama and romance. The chord progression of Bb7, Eb, and Ab contributes to the relaxing atmosphere throughout the song."],
        ["An energetic and melodic electronic trance track with a space and retro vibe, featuring drums, distortion guitar, flute, synth bass, and slap bass. Set in A minor with a fast tempo of 138 BPM, the song maintains a 4/4 time signature throughout its duration."],
        ["This short electronic song in C minor features a brass section, string ensemble, tenor saxophone, clean electric guitar, and slap bass, creating a melodic and slightly dark atmosphere. With a tempo of 124 BPM (Allegro) and a 4/4 time signature, the track incorporates a chord progression of C7/E, Eb6, and Bbm6, adding a touch of corporate and motivational vibes to the overall composition."],
        ["An energetic and melodic electronic trance track with a space and retro vibe, featuring drums, distortion guitar, flute, synth bass, and slap bass. Set in A minor with a fast tempo of 138 BPM, the song maintains a 4/4 time signature throughout its duration."],
        ["A short but energetic rock fragment in C minor, featuring overdriven guitars, electric bass, and drums, with a vivacious tempo of 155 BPM and a 4/4 time signature, evoking a blend of dark and melodic tones."],
    ],
    cache_examples="lazy",
    css=".example-caption { text-align: left; }"
)
app.launch()
