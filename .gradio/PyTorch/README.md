# Image Classification in PyTorch
Image classification is a central task in computer vision. Building better classifiers to classify what object is present in a picture is an active area of research, as it has applications stretching from autonomous vehicles to medical imaging.

Such models are perfect to use with Gradio's image input component. In this tutorial, we will build a web demo to classify images using Gradio. We can build the whole web application in Python.

## Step 1: Setting up the image classification model
First, we will need an image classification model. For this tutorial, we will use a pretrained Resnet-18 model, as it is easily downloadable from PyTorch Hub. You can use a different pretrained model or train your own.
```import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()```

## Step 2: Defining a predict function
Next, we will need to define a function that takes in the user input, which in this case is an image, and returns the prediction. The prediction should be returned as a dictionary whose keys are class name and values are confidence probabilities. We will load the class names from this text file.

* inp: the input image as a PIL image

The function converts the input image into a PIL Image and subsequently into a PyTorch tensor. After processing the tensor through the model, it returns the predictions in the form of a dictionary named confidences. The dictionary's keys are the class labels, and its values are the corresponding confidence probabilities.

In this section, we define a predict function that processes an input image to return prediction probabilities. The function first converts the image into a PyTorch tensor and then forwards it through the pretrained model. We use the softmax function in the final step to calculate the probabilities of each class. The softmax function is crucial because it converts the raw output logits from the model, which can be any real number, into probabilities that sum up to 1. This makes it easier to interpret the model's outputs as confidence levels for each class.

Step 3: Creating a Gradio interface
Now that we have our predictive function set up, we can create a Gradio Interface around it.

In this case, the input component is a drag-and-drop image component. To create this input, we use Image(type=“pil”) which creates the component and handles the preprocessing to convert that to a PIL image.

The output component will be a Label, which displays the top labels in a nice form. Since we don't want to show all 1,000 class labels, we will customize it to show only the top 3 images by constructing it as Label(num_top_classes=3).

Finally, we'll add one more parameter, the examples, which allows us to prepopulate our interfaces with a few predefined examples. The code for Gradio looks like this:


import gradio as gr
gr.Interface(fn=predict,
       inputs=gr.Image(type="pil"),
       outputs=gr.Label(num_top_classes=3),
       examples=["/content/lion.jpg", "/content/cheetah.jpg"]).launch()

Copied!
Wrap Toggled!
The example paths provided, /content/lion.jpg and /content/cheetah.jpg, are placeholders. You should replace these with the actual paths to images on your system or server where you have saved the images you want to use for testing. This ensures that when you or others are using the Gradio interface, the examples are correctly loaded and can be used to demonstrate the functionality of your image classifier.

This produces the following interface, which you can try in a browser (try uploading your own examples).




And you're done! That's all the code you need to build a web demo for an image classifier. If you'd like to share with others, try setting share=True when you launch() the Interface!

Conclusion
Gradio simplifies the process of building interactive web demos for machine learning models. By integrating Gradio with models like BLIP for image captioning, you can create practical, user-friendly applications that leverage the power of AI to solve real-world problems. This tool not only aids in demonstrating the capabilities of your models but also in collecting valuable feedback for further improvement.



