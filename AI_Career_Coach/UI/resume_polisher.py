# Import necessary packages
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
import gradio as gr

# Model and project settings
model_id = "meta-llama/llama-3-2-11b-vision-instruct"  # Directly specifying the LLAMA3 model

# Set credentials to use the model
credentials = Credentials(
                   url = "https://us-south.ml.cloud.ibm.com",
                  )

# Generation parameters
params = TextChatParameters(
    temperature=0.7,
    max_tokens=512
)

project_id = "skills-network"  # Specifying project_id as provided

# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

# Function to polish the resume using the model, making polish_prompt optional
def polish_resume(position_name, resume_content, polish_prompt=""):
    # Check if polish_prompt is provided and adjust the combined_prompt accordingly
    if polish_prompt and polish_prompt.strip():
        prompt_use = f"Given the resume content: '{resume_content}', polish it based on the following instructions: {polish_prompt} for the {position_name} position."
    else:
        prompt_use = f"Suggest improvements for the following resume content: '{resume_content}' to better align with the requirements and expectations of a {position_name} position. Return the polished version, highlighting necessary adjustments for clarity, relevance, and impact in relation to the targeted role."
    
    messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_use
            },
        ]
    }
]   
    # Generate a response using the model with parameters
    generated_response = model.chat(messages=messages)

    # Extract and return the generated text
    generated_text = generated_response['choices'][0]['message']['content']
    
    return generated_text

# Create Gradio interface for the resume polish application, marking polish_prompt as optional
resume_polish_application = gr.Interface(
    fn=polish_resume,
    flagging_mode="never", # Deactivate the flag function in gradio as it is not needed.
    inputs=[
        gr.Textbox(label="Position Name", placeholder="Enter the name of the position..."),
        gr.Textbox(label="Resume Content", placeholder="Paste your resume content here...", lines=20),
        gr.Textbox(label="Polish Instruction (Optional)", placeholder="Enter specific instructions or areas for improvement (optional)...", lines=2),
    ],
    outputs=gr.Textbox(label="Polished Content"),
    title="Resume Polish Application",
    description="This application helps you polish your resume. Enter the position your want to apply, your resume content, and specific instructions or areas for improvement (optional), then get a polished version of your content."
)

# Launch the application
resume_polish_application.launch()

# INPUT 
# > Technical corporate training position
# > ERIC CAREER CHANGER
# 973.761.9355 ƒ ecareerchanger@noemail.yescom
# www.linkedin.com/me/profile
# OBJECTIVE: Technical corporate training position in the healthcare industry
# HIGHLIGHTS OF QUALIFICATIONS
# Nine years of technical experience with corporate clients, including Fortune 500 healthcare organizations
# Managed major sales account for a regional hospital ranked in ³Top 100´ healthcare facilities
# Skilled in training and supervision of professional and administrative staff
# Expertise in technical operations, including wide range of hardware and software systems
# Strong presentation, customer service and communication skills
# PROFESSIONAL ACCOMPLISHMENTS
# HUMAN RESOURCE/COMMUNICATION
# x Supervised and trained over 150 personnel within departments averaging 25 professional staff
# x Trained over 50 supervisors and managers annually on technical hardware for inventory control
# x Collaborated with upper level management and human resource departments in diverse industries
# x Assisted individual and corporate clients with understanding of technical components of purchases
# x Represented company at regional and national trade shows with new products
# ORGANIZATION/PLANNING
# x Revised policy manuals and developed curricula for Fortune 500 sales training programs
# x Designed and implemented educational and entertainment software for testing by research department
# x Developed systems for microcomputers and smartphones that are currently in use by organizations
# MARKETING/SALES
# x Managed sales account for large regional hospital with annual sales exceeding $20 million
# x Marketed personal computer hardware and software systems to Fortune 500 companies
# x Developed and implemented advertising and marketing strategies to increase sales
# x Recognized for exceeding sales expectations by as much as 75%; received numerous outstanding performance awards
# EMPLOYMENT HISTORY
# Marketing/Sales Representative, Microcomputers, Inc., Fairfield, NJ June 20xx - present
# Computer Distribution Coordinator, Computers Unlimited, Livingston, NJ May 20xx - August 20xx
# Management Trainee, Computer Systems, LLC, Edison, NJ August 20xx - May 20xx
# EDUCATION
# Seton Hall University, Stillman School of Business, South Orange, NJ
# Bachelor of Science in Business Administration, May 20xx
# Concentration: Management Minor: Computer Science
# PROFESSIONAL AFFILIATIONS
# President, American Marketing Association, New Jersey Chapter, May 20xx - present
# Member, Computing Technology Industry Association (CompTIA), September 20xx - present

# OUTPUT
# **Polished Resume Version:**

# **ERIC CAREER CHANGER**
# 973.761.9355 | ecareerchanger@noemail.yescom | www.linkedin.com/me/profile
# **OBJECTIVE:**
# To leverage my technical expertise and corporate training experience to secure a Technical Corporate Training position in the healthcare industry, where I can develop and deliver training programs that enhance employee performance and drive business success.

# **SUMMARY:**
# Results-driven technical professional with 9 years of experience in corporate training, sales, and management, including working with Fortune 500 healthcare organizations. Proven track record of developing and delivering effective training programs, leading cross-functional teams, and driving business growth through sales and marketing initiatives.

# **HIGHLIGHTS OF QUALIFICATIONS:**

# * 9 years of technical experience in corporate training, sales, and management, with expertise in a wide range of hardware and software systems
# * Proven ability to develop and deliver training programs that enhance employee performance and drive business success
# * Strong presentation, customer service, and communication skills
# * Experience working with Fortune 500 healthcare organizations, including managing major sales accounts and collaborating with upper-level management and human resource departments

# **PROFESSIONAL ACCOMPLISHMENTS:**

# * **Training and Development:**
#  + Developed and delivered training programs for over 150 personnel, including supervisors and managers, on technical hardware and software systems
#  + Collaborated with research department to design and implement educational and entertainment software for testing
#  + Revised policy manuals and developed curricula for Fortune 500 sales training programs
# * **Leadership and Management:**
#  + Supervised and trained professional staff, including developing systems for microcomputers and smartphones
#  + Collaborated with upper-level management and human resource departments in diverse industries
#  + Managed sales account for large regional hospital, exceeding sales expectations by up to 75%
# * **Marketing and Sales:**
#  + Marketed personal computer hardware and software systems to Fortune 500 companies
#  + Developed and implemented advertising and marketing strategies to increase sales
#  + Recognized for outstanding performance and received numerous awards

# **EMPLOYMENT HISTORY:**

# * **Marketing/Sales Representative, Microcomputers, Inc., Fairfield, NJ** (June 20xx - present)
# * **Computer Distribution Coordinator, Computers Unlimited, Livingston, NJ** (May 20xx - August 20xx)
# * **Management Trainee, Computer Systems, LLC, Edison, NJ** (August 20xx - May 20xx)

# **EDUCATION:**

# * **Bachelor of Science in Business Administration**, Seton