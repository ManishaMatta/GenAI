import gradio as gr

def add_numbers(Num1, Num2):
    return Num1 + Num2

# Define the interface
# demo = gr.Interface(
#     fn=add_numbers, 
#     inputs=["number", "number"], # Create two numerical input fields where users can enter numbers
#     outputs="number" # Create numerical output fields
# )

def combine(a, b):
    return a + " " + b
    
demo = gr.Interface(
    fn=combine,
    inputs = [
        gr.Textbox(label="Input 1"),
        gr.Textbox(label="Input 2")
    ],
    outputs = gr.Textbox(value="", label="Output")
)

# Launch the interface
demo.launch(server_name="0.0.0.0", server_port= 7860)