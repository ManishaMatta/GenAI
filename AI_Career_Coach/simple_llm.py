############################################################################################################################################################
# Create a Q&A bot
# This tutorial will walk you through the process of creating a Q&A chatbot leveraging the llama-3-2-11b-vision-instruct model developed by Meta. This powerful foundation model has been seamlessly integrated into IBM's watsonx.ai platform, simplifying your development journey. Our provided API eliminates the need for generating complex API tokens, streamlining the application creation process. The llama-3-2-11b-vision-instruct model is equipped with features designed to
# Supports Q&A
# Summarization
# Classification
# Generation
# Extraction
# Retrieval-Augmented Generation tasks
# This model aligns perfectly with our objective for the application being created.
# Note: The llama-3-2-11b-vision-instruct model, like any AI technology, has its limitations, and it is possible to encounter nonsensical responses occasionally. The primary objective of this project is to provide guidence on utilizing LLMs with watsonx.ai.
# Follow these step-by-step instructions to create your application:
# Still in the PROJECT directory, create a new Python file named simple_llm.py (you are welcome to choose a different name if you prefer).
# Enter the following script content into your newly created simple_llm.py file and save your changes. Line-by-line explanation of the code snippet is provided.

# In the code, we simply used "skills-network" as project_id to gain immediate, free access to the API without the need for initial registration. It's important to note that this access method is exclusive to this Cloud IDE environment.
#  If you are interested in using the model/API in a local environment, detailed instructions and further information are available in this tutorial.
#  https://medium.com/the-power-of-ai/ibm-watsonx-ai-the-interface-and-api-e8e1c7227358
############################################################################################################################################################
#  Execution endpoint : http://127.0.0.1:7860
#  /Users/Z00FC77/.pyenv/versions/3.12.2/bin/python /Users/Z00FC77/Documents/Personal/gitHub/ManishaMatta/GenAI/AI_Career_Coach/simple_llm.py
############################################################################################################################################################
# EXAMPLE 1 Create a Q&A bot
############################################################################################################################################################
# Import necessary packages
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

# Model and project settings
model_id = "meta-llama/llama-3-2-11b-vision-instruct"  # Directly specifying the LLAMA3 model

# Set credentials to use the model
credentials = Credentials(url = "https://us-south.ml.cloud.ibm.com",)

# Set necessary parameters
params = TextChatParameters()

# Specifying project_id as provided Cloud IDE
project_id = "skills-network"  
# https://medium.com/the-power-of-ai/ibm-watsonx-ai-the-interface-and-api-e8e1c7227358

# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)
prompt_txt = "How to be a good Data Scientist?"  # Your question

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_txt
            },
        ]
    }
]

# Attempt to generate a response using the model with overridden parameters
generated_response = model.chat(messages=messages)
generated_text = generated_response['choices'][0]['message']['content']

# Print the generated response
print(generated_text)

############################################################################################################################################################


############################################################################################################################################################

############################################################################################################################################################