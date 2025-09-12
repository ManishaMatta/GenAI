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

project_id = "skills-network"

# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

# Function to generate a customized cover letter
def generate_cover_letter(company_name, position_name, job_description, resume_content):
    # Craft the prompt for the model to generate a cover letter
    prompt = f"Generate a customized cover letter using the company name: {company_name}, the position applied for: {position_name}, and the job description: {job_description}. Ensure the cover letter highlights my qualifications and experience as detailed in the resume content: {resume_content}. Adapt the content carefully to avoid including experiences not present in my resume but mentioned in the job description. The goal is to emphasize the alignment between my existing skills and the requirements of the role."

    messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt
            },
        ]
    }
]   

    # Generate a response using the model with parameters
    generated_response = model.chat(messages=messages)

    # Extract and return the generated text
    cover_letter = generated_response['choices'][0]['message']['content']

    return cover_letter

# Create Gradio interface for the cover letter generation application
cover_letter_app = gr.Interface(
    fn=generate_cover_letter,
    flagging_mode="never", # Deactivate the flag function in gradio as it is not needed.
    inputs=[
        gr.Textbox(label="Company Name", placeholder="Enter the name of the company..."),
        gr.Textbox(label="Position Name", placeholder="Enter the name of the position..."),
        gr.Textbox(label="Job Description Information", placeholder="Paste the job description here...", lines=10),
        # gr.Textbox(label="Job Skills Keywords", placeholder="Paste the job required skills keywords here...", lines=2),
        gr.Textbox(label="Resume Content", placeholder="Paste your resume content here...", lines=10),
    ],
    outputs=gr.Textbox(label="Customized Cover Letter"),
    title="Customized Cover Letter Generator",
    description="Generate a customized cover letter by entering the company name, position name, job description and your resume."
)

# Launch the application
cover_letter_app.launch()


# INPUT
# > https://corporate.target.com/jobs/w94/85/on-demand-guest-advocate-cashier-,-general-merchandise,-fulfillment-t3368
# > Target
# > On-Demand: Guest Advocate (Cashier), General Merchandise, Fulfillment (T3368)
# > Job Id: R0000369485

# Starting Hourly Rate / Salario por Hora Inicial: $18.25 USD per hour

# ALL ABOUT TARGET

# Working at Target means helping all families discover the joy of everyday life. We bring that vision to life through our values and culture. Learn more about Target here.

# ALL ABOUT ON DEMAND

# You can work as much or as little as you like as an On-Demand TM and your schedule may vary depending on shift availability and store needs. This role is ideal for those that are looking for a personalized work schedule.

# As an On-Demand TM you will not be included on the posted weekly schedule, but rather will have the opportunity to create your own schedule by picking up shifts posted by leaders or other team members (via our myTime mobile scheduling app) that work best with your schedule.

# We require your active engagement by picking up and working shifts as well as responding to our attempts at contact.

# We will contact you throughout the year (via your provided contact information) and confirm your interest in working shifts at Target. If we do not receive a response to our communication attempts, your employment with Target will be administratively terminated.

# Regular attendance is necessary and we require your active engagement by picking up and working shifts once every 4 weeks (minimum of four hours). Flexibility can be granted if you are unable to work once every 4 weeks due to a personal circumstance, but you are required to respond to our attempts to contact you to confirm your interest in working shifts at Target. You must work at least one shift within 6 months or you will be administratively terminated. Effective December 2024, you must work at least one shift within 5 months or you will be administratively terminated.

# Your communication and ability to work when our business demands it most are critical to your success in this role.

# Should you be offered a position as an On-Demand TM, you will be required to attend a Target Welcome orientation and commit to a short-term structured training schedule to ensure you are properly prepared for your new role. After that, the myTime mobile scheduling app is where you can pick up the shifts you desire to work.

# ALL ABOUT SMALL FORMATS

# We enable a consistent experience for our guests by ensuring product is in stock, available, accurately priced and signed on the sales floor in our smallest format stores. Experts of service, operations, process and efficiency, this team is responsible for being proficient in all areas of the store to complete duties such as, but not limited to, cashiering, stocking, presentation and price accuracy. You’ll provide exceptional guest service, customizing each experience and anticipating guest needs.

# At Target, we believe in our team members having meaningful experiences that help them build and develop skills for a career. The role of a Small Format Team Member can provide you with the:

# Knowledge of guest service fundamentals and experience building a guest first culture across the store
# Experience in retail business fundamentals including: department sales trends, pricing and promotion strategies, inventory management, and process efficiency & improvement
# Experience supporting daily/weekly workload to support business priorities and deliver on sales goals
# As a Small Format Team Member, no two days are ever the same, but a typical day will most likely include the following responsibilities:

# Create a welcoming experience by authentically greeting all guests
# Observe to quickly understand whether a guest needs assistance or wants to interact. Follow body language and verbal cues to tailor your approach.
# Engage with guests in a genuine way, which includes asking questions to better understand their specific needs.
# Be knowledgeable about the tools, products, and services available in the total store, and specific to your area, to solve issues for the guest and improve their experience.
# Thank the guest in a genuine way and let them know we’re happy they chose to shop at Target.
# Help guests as you complete workload with minimal guest disruption
# Work in all departments to ensure sales floor is full, zoned and in stock for guests
# Push and stock product to sales floor
# Execute adjacency changes, transitions, revisions and sales plans for all departments
# Conduct weekly price change workload and ensure regular and promotional signing is set accurately for all departments
# Complete scans and system audit functions to ensure inventory accuracy
# Support execution of major transitions and ISM
# Maintain interior and exterior brand, including emptying garbage cans and attending to restroom cleanliness, collecting carts, charging electronic carts, RVM maintenance (if applicable) and attending to spills throughout the store as needed.
# Accurately execute all pulls (i.e., daily Fills, out of stock, manual and guest requests) and backstock product from all departments
# Process all inbound deliveries (using the receive application) to ensure inventory accuracy
# Complete all backroom weekly audits
# Operate power equipment only if certified
# Maintain backroom organization and location accuracy and follow equipment guidelines
# Follow processes accurately with attention to detail, monitor own progress and accurately prioritize tasks
# Demonstrate a culture of ethical conduct, safety and compliance
# Work in a safe manner at all times to benefit yourself and others; identify and correct hazards; comply with all safety policies and best practices.
# Support guest services such as back-up cashier, order pick up (OPU) and Drive-up (DU) and maintain a compliance culture while executing those duties, such as compliance with federal, state, and local adult beverage laws
# All other duties based on business needs
# WHAT WE ARE LOOKING FOR

# We might be a great match if:

# Working in a fun and energetic environment makes you excited…. We work efficiently and as a team to deliver for our guests
# Providing service to our guests that makes them say I LOVE TARGET! excites you…. That’s why we love working at Target
# Stocking, Setting and Selling Target products sounds like your thing… That’s the core of what we do
# You aren’t looking for Monday thru Friday job where you are at a computer all day… We are busy all day (especially on the weekends), making it easy for the guest to feel welcomed, inspired and rewarded
# The good news is that we have some amazing training that will help teach you everything you need to know to be a Small Format Team Member. However, there are a few skills you should have from the get-go:

# Capability to remain focused and composed in a fast-paced environment and accomplish multiple tasks within established timeframes.
# Welcoming and helpful attitude toward guests and other team members
# Ability to communicate on multiple frequency devices and operate handheld scanners, and other technology equipment as directed.
# Work both independently and with a team
# Resolve guest questions quickly on the spot
# Attention to detail and follow a multi-step process
# We are an awesome place to work and care about our teams, so we want to make sure we are clear on a few more basics that we expect:

# Accurately handle cash register operations as needed.
# Climb up and down ladders safely
# Scan, handle and move merchandise efficiently and safely, including frequently lifting or moving merchandise up to 15 pounds and occasionally lifting or moving merchandise and fixtures up to 44 pounds without additional assistance from others.
# Flexible work schedule (e.g., nights, weekends and holidays); reliable and prompt attendance necessary.
# You can work as much or as little as you like as an on-demand TM, however, we ask for your active engagement by picking up and working shifts (via our myTime mobile App) every 4 weeks, as well as responding at our attempts at contact. We will contact you throughout the year (via your provided contact information) and confirm your ability and interest in working shifts at Target. If we do not receive a response your employment with Target will be administratively terminated. You must work at least one shift within 6 months or you will be administratively terminated. Effective December 2024, you must work at least one shift within 5 months or you will be administratively terminated.
# Capable of working in and exposure to varying temperatures, humidity, and other elements while performing certain job duties including but not limited to Drive-Up, carryout, etc.
# Ability to remain mobile for the duration of a scheduled shift (shift length may vary).
# Find competitive benefits from financial and education to well-being and beyond at https://corporate.target.com/careers/benefits.
# > **Polished Resume Version:**

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

# OUTPUT
# Here's a customized cover letter tailored to the On-Demand Guest Advocate (Cashier), General Merchandise, Fulfillment position at Target:

# [Your Name]
# [Your Address]
# [City, State ZIP Code]
# [Date]

# Hiring Manager
# Target Corporation
# [Target Store Address]
# [City, State ZIP Code]

# Dear Hiring Manager,

# I am excited to apply for the On-Demand Guest Advocate (Cashier), General Merchandise, Fulfillment position (Job Id: R0000369485) at Target. As a highly motivated and results-driven professional with a strong background in customer service, sales, and technical training, I am confident that I would be an excellent fit for this role.

# With over 9 years of experience in corporate training, sales, and management, I possess the skills and expertise required to excel as a Guest Advocate. My ability to develop and deliver effective training programs, lead cross-functional teams, and drive business growth through sales and marketing initiatives will enable me to make a positive impact on the Target team.

# As a technical professional, I am comfortable working with various hardware and software systems, which will serve me well in handling the technical aspects of the Guest Advocate role. My strong presentation, customer service, and communication skills will allow me to provide exceptional guest service and create a welcoming experience for all customers.

# I am particularly drawn to this role because of the opportunity to work in a fast-paced environment, where no two days are ever the same. I thrive in dynamic settings and am comfortable adapting to changing circumstances, which will enable me to excel in this position. My ability to remain focused and composed in high-pressure situations will ensure that I provide top-notch service to our guests.

# In addition to my technical expertise and customer service skills, I am a strong communicator and team player. I am confident that my ability to work effectively with others, both independently and as part of a team, will enable me to make a positive contribution to the Target team.

# I am impressed by Target's commitment to creating a welcoming and inclusive environment for all guests, and I am excited about the opportunity to be a part of a team that shares my values. I am confident that my skills, experience, and passion for delivering exceptional guest service make me an ideal candidate for this role.

# Thank you for considering my application. I would welcome the opportunity to discuss this position further and explain in greater detail why I am the ideal candidate for this role.

# Sincerely,

# Eric Career Changer
# 973.761.9355 | ecareerchanger@noemail