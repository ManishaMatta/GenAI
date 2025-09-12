# calculate the sum of your input numbers.
############################################################################################################################################################
#  Execution endpoint : http://127.0.0.1:7860
#  /Users/Z00FC77/.pyenv/versions/3.12.2/bin/python /Users/Z00FC77/Documents/Personal/gitHub/ManishaMatta/GenAI/AI_Career_Coach/gradio_demo.py
############################################################################################################################################################
# EXAMPLE 1: Simple addition of two numbers using Gradio interface
############################################################################################################################################################
# import gradio as gr

# def add_numbers(Num1, Num2):
#     return Num1 + Num2

# # Define the interface
# demo = gr.Interface(
#     fn=add_numbers, 
#     inputs=["number", "number"], # Create two numerical input fields where users can enter numbers
#     outputs="number" # Create numerical output fields
# )

# # Launch the interface
# demo.launch(server_name="127.0.0.1", server_port= 7860)
############################################################################################################################################################
# EXAMPLE 1: Combine 2 sentences
############################################################################################################################################################
import gradio as gr

def combine_sentence(text1, text2):
    return text1 + " " + text2

# Define the interface
demo = gr.Interface(
    fn=combine_sentence, 
    # inputs=["text", "text"], # Create two text input fields where users can enter numbers
    # outputs="text" # Create text output fields
    inputs = [
        gr.Textbox(label="Input 1"),
        gr.Textbox(label="Input 2")
    ],
    outputs = gr.Textbox(value="", label="Output")
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)
############################################################################################################################################################