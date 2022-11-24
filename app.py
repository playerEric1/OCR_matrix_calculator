import os
import gradio as gr
from PIL import Image

os.system("pip install pix2tex")
from pix2tex import cli as pix2tex

# Load model
model = pix2tex.LatexOCR()


def inference(path):
    img = Image.open(path)
    output = model(img)
    print("Model output:", output)
    return output


# Front end
title = "Convert images of equations into LaTeX code 📚✖️➕ 🔢"
description = "<div> Did you come across a complex mathematical expression that you want to refer to in your " \
              "report/thesis? Is your freemium over at <a href='https://mathpix.com/' target='_blank'>Mathpix</a>? 😫 " \
              "<br><br> Take a screenshot of the equation and use this application to convert it into LaTeX code. 😎  " \
              "To use it, simply upload your screenshot/equation image, or click one of the examples to load them. To " \
              "verify the results, copy & paste the output in <a href='https://quicklatex.com/' target='_blank'>Quick " \
              "LaTeX</a>. Read more at the links below. If ERROR, please try again.</div> "
article = "<p style='text-align: center'><a href='' " \
          "target='_blank'>pix2tex: Using a ViT to convert images of equations into LaTeX code</a> | <a " \
          "href='' target='_blank'>Github</a></p> "


# UI
demo = gr.Interface(
    inference,
    title=title,
    description=description,
    article=article,
    inputs=gr.inputs.Image(
        type="filepath", label="Input: Image of your equation you want to covert."
    ),
    outputs=gr.outputs.Textbox(type="text", label="Output: Converted LaTeX code."),
    examples=["./eqn1.png", "./eqn2.png", "./eqn3.png"],
    allow_flagging="never",
    analytics_enabled=False,
)
demo.launch(enable_queue=True, share=True)
