# Import necessary packages
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

# Model and project settings
model_id = "meta-llama/llama-3-2-11b-vision-instruct"  # Directly specifying the LLAMA3 model

# Set credentials to use the model
credentials = Credentials(
                   url = "https://us-south.ml.cloud.ibm.com",
                  )

# Set necessary parameters
params = TextChatParameters()

# Specifying project_id as provided
project_id = "skills-network"  


# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)
prompt_txt = "How to be a good Data Scientist?"  # Your question
# prompt_txt = "How to get promotion?"  # Your question

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

# OUTPUT
# To be a good data scientist, you'll need to possess a combination of technical, business, and soft skills. Here are some key areas to focus on:
# **Technical Skills:**

# 1. **Programming languages:** Proficiency in languages such as Python, R, SQL, and Julia.
# 2. **Data manipulation and analysis:** Familiarity with data structures, statistical modeling, and machine learning algorithms.
# 3. **Data visualization:** Ability to create interactive and informative visualizations using tools like Tableau, Power BI, or D3.js.
# 4. **Big data technologies:** Knowledge of Hadoop, Spark, and NoSQL databases.
# 5. **Deep learning:** Familiarity with frameworks like TensorFlow, PyTorch, or Keras.

# **Mathematical and Statistical Skills:**

# 1. **Linear Algebra:** Understanding of vector spaces, linear transformations, and matrix operations.
# 2. **Calculus:** Familiarity with derivatives, integrals, and optimization techniques.
# 3. **Statistics:** Knowledge of probability distributions, statistical inference, and hypothesis testing.
# 4. **Machine learning theory:** Understanding of the theoretical foundations of machine learning.

# **Business Skills:**

# 1. **Communication:** Ability to effectively communicate complex technical concepts to non-technical stakeholders.
# 2. **Project management:** Experience with project planning, execution, and delivery.
# 3. **Business acumen:** Understanding of business objectives, industries, and markets.
# 4. **Stakeholder management:** Ability to collaborate with cross-functional teams and stakeholders.

# **Soft Skills:**

# 1. **Problem-solving:** Ability to approach complex problems in a methodical and creative way.
# 2. **Critical thinking:** Capacity to analyze data, identify patterns, and draw meaningful conclusions.
# 3. **Collaboration:** Willingness to work with others, share knowledge, and learn from others.
# 4. **Adaptability:** Flexibility in adapting to new tools, technologies, and methodologies.
# 5. **Continuous learning:** Commitment to staying up-to-date with industry trends, technologies, and best practices.

# **Additional Tips:**

# 1. **Practice data science:** Apply your skills to real-world problems and projects.
# 2. **Read industry blogs and books:** Stay informed about the latest developments in data science and AI.
# 3. **Network with professionals:** Attend conferences, meetups, and join online communities to connect with other data scientists.
# 4. **Participate in hackathons and competitions:** Showcase your skills and learn from others.
# 5. **Pursue certifications:** Consider obtaining certifications like Certified Data Scientist (CDS) or Certified Analytics Professional (CAP) to demonstrate your expertise.

# By focusing on these areas, you'll be well on your way to becoming a proficient and effective data scientist.
# ''' 