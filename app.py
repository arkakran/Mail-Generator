# import streamlit as st
# import os
# import json
# from datetime import datetime
# import requests
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Set up Groq API key
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # App title and description
# st.set_page_config(page_title="Student Email Assistant", page_icon="✉️", layout="wide")
# st.title("✉️ AI-Powered Email & Networking Assistant for Students")
# st.markdown("Generate professional emails and messages for your academic and career needs")

# # Initialize session state for history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Function to generate email using Groq
# def generate_email(email_type, context_data):
#     prompt_templates = {
#         "cold_email": """
#         Write a professional cold email to a recruiter for a job/internship opportunity.
        
#         Company: {company}
#         Position: {position}
#         Recipient: {recipient}
#         Student Background: {background}
#         Key Points to Highlight: {key_points}
        
#         The email should be professional, concise, and compelling. Include a clear subject line.
#         """,
        
#         "linkedin_message": """
#         Write a concise LinkedIn message for {purpose}.
        
#         Recipient: {recipient}
#         Student Background: {background}
#         Connection Context: {connection_context}
#         Key Points: {key_points}
        
#         Keep it under 300 characters, professional yet personable, and with a clear call to action.
#         """,
        
#         "academic_email": """
#         Write a formal email to a {recipient_role} at a university.
        
#         Recipient Name: {recipient}
#         Purpose: {purpose}
#         Course/Program Details: {course_details}
#         Key Information: {key_information}
        
#         The email should be respectful, formal, and clearly structured with an appropriate subject line.
#         """,
        
#         "cover_letter": """
#         Write a professional cover letter for a {position} position at {company}.
        
#         Student Background: {background}
#         Key Skills & Experiences: {key_skills}
#         Job Description Highlights: {job_description}
        
#         The cover letter should be compelling, highlight relevant experiences and skills, and express genuine interest in the role.
#         """,
        
#         "follow_up": """
#         Write a follow-up email regarding {previous_interaction}.
        
#         Recipient: {recipient}
#         Previous Communication Date: {prev_date}
#         Context: {context}
#         Purpose of Follow-up: {purpose}
        
#         The email should be polite, concise, reference the previous interaction, and include a clear next step.
#         """
#     }
    
#     # Format the prompt with the context data
#     formatted_prompt = prompt_templates[email_type].format(**context_data)
    
#     # Call Groq API via REST API
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
    
#     payload = {
#         "messages": [
#             {"role": "system", "content": "You are a professional email assistant for students. Write emails that are clear, concise, and effective."},
#             {"role": "user", "content": formatted_prompt}
#         ],
#         "model": "llama3-70b-8192",  # Using LLaMA 3 70B model from Groq
#         "temperature": 0.7,
#         "max_tokens": 1000
#     }
    
#     response = requests.post(
#         "https://api.groq.com/openai/v1/chat/completions",
#         headers=headers,
#         json=payload
#     )
    
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         st.error(f"Error from Groq API: {response.text}")
#         return "Error generating email. Please try again."

# # Sidebar for email type selection
# with st.sidebar:
#     st.header("Email Type")
#     email_type = st.selectbox(
#         "Select the type of message you need",
#         ["cold_email", "linkedin_message", "academic_email", "cover_letter", "follow_up"],
#         format_func=lambda x: {
#             "cold_email": "Cold Email to Recruiters",
#             "linkedin_message": "LinkedIn Short Message",
#             "academic_email": "Email to University Authority",
#             "cover_letter": "Cover Letter Generator",
#             "follow_up": "Follow-up Email"
#         }[x]
#     )
    
#     st.divider()
#     st.header("History")
#     if st.session_state.history:
#         for i, item in enumerate(st.session_state.history):
#             if st.button(f"{item['type']} - {item['date']}", key=f"history_{i}"):
#                 st.session_state.selected_history = item

# # Main content area
# col1, col2 = st.columns([1, 1])

# # Input form based on selected email type
# with col1:
#     st.header("Input Information")
    
#     with st.form(key="email_form"):
#         context_data = {}
        
#         if email_type == "cold_email":
#             context_data["company"] = st.text_input("Company Name")
#             context_data["position"] = st.text_input("Position/Role")
#             context_data["recipient"] = st.text_input("Recruiter Name (if known)")
#             context_data["background"] = st.text_area("Your Background (education, skills, etc.)")
#             context_data["key_points"] = st.text_area("Key Points to Highlight")
            
#         elif email_type == "linkedin_message":
#             context_data["purpose"] = st.selectbox("Message Purpose", 
#                 ["Connection Request", "Job Inquiry", "Informational Interview", "Thank You", "Follow-up"])
#             context_data["recipient"] = st.text_input("Recipient Name")
#             context_data["connection_context"] = st.text_input("How you found/know this person")
#             context_data["background"] = st.text_input("Brief introduction about yourself")
#             context_data["key_points"] = st.text_area("Key message points (brief)")
            
#         elif email_type == "academic_email":
#             context_data["recipient_role"] = st.selectbox("Recipient Role", 
#                 ["Professor", "Dean", "Administrator", "Academic Advisor", "Department Chair"])
#             context_data["recipient"] = st.text_input("Recipient Name")
#             context_data["purpose"] = st.selectbox("Email Purpose",
#                 ["Recommendation Letter", "Extension Request", "Scholarship Inquiry", 
#                  "Research Opportunity", "Grade Appeal", "General Question"])
#             context_data["course_details"] = st.text_input("Course/Program Details")
#             context_data["key_information"] = st.text_area("Key Information to Include")
            
#         elif email_type == "cover_letter":
#             context_data["position"] = st.text_input("Position Title")
#             context_data["company"] = st.text_input("Company Name")
#             context_data["background"] = st.text_area("Your Background (education, experience)")
#             context_data["key_skills"] = st.text_area("Key Skills & Relevant Experiences")
#             context_data["job_description"] = st.text_area("Key Points from Job Description")
            
#         elif email_type == "follow_up":
#             context_data["previous_interaction"] = st.selectbox("Previous Interaction", 
#                 ["Job Application", "Interview", "Networking Event", "Informational Meeting", "Unanswered Email"])
#             context_data["recipient"] = st.text_input("Recipient Name")
#             context_data["prev_date"] = st.date_input("Date of Previous Communication")
#             context_data["context"] = st.text_area("Context of Previous Interaction")
#             context_data["purpose"] = st.text_input("Purpose of Follow-up")
        
#         submit_button = st.form_submit_button("Generate Email")

# # Output area
# with col2:
#     st.header("Generated Email")
    
#     if submit_button:
#         with st.spinner("Generating your professional email..."):
#             try:
#                 # Generate the email
#                 generated_email = generate_email(email_type, context_data)
                
#                 # Save to history
#                 history_item = {
#                     "type": email_type,
#                     "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
#                     "context": context_data,
#                     "email": generated_email
#                 }
#                 st.session_state.history.insert(0, history_item)  # Add to start of list
                
#                 # Display the generated email
#                 st.text_area("Your email is ready!", generated_email, height=400)
                
#                 # Add options to copy or download
#                 st.download_button(
#                     label="Download as Text",
#                     data=generated_email,
#                     file_name=f"{email_type}_{datetime.now().strftime('%Y%m%d')}.txt",
#                     mime="text/plain"
#                 )
                
#             except Exception as e:
#                 st.error(f"Error generating email: {str(e)}")
    
#     # Display history item if selected
#     if 'selected_history' in st.session_state:
#         st.subheader("From History")
#         st.text_area("Saved email", st.session_state.selected_history["email"], height=400)
        
# # Additional features section
# st.header("Tips for Professional Communication")
# tips_tab1, tips_tab2, tips_tab3 = st.tabs(["Email Etiquette", "LinkedIn Best Practices", "Follow-up Timing"])

# with tips_tab1:
#     st.markdown("""
#     ### Email Etiquette for Students
#     * Use a professional email address
#     * Create clear, descriptive subject lines
#     * Address recipients properly (Dr., Prof., Mr., Ms.)
#     * Keep emails concise and to the point
#     * Proofread before sending
#     * Include a professional signature
#     """)

# with tips_tab2:
#     st.markdown("""
#     ### LinkedIn Messaging Tips
#     * Keep messages under 300 characters for cold outreach
#     * Personalize each connection request
#     * Mention shared connections or interests
#     * Be clear about your purpose
#     * Follow up only once if you don't receive a response
#     """)

# with tips_tab3:
#     st.markdown("""
#     ### Follow-up Timing Guidelines
#     * After job application: 1 week
#     * After interview: 24-48 hours for thank you, 1 week for status update
#     * Networking follow-up: 24-48 hours
#     * Unanswered emails: 3-5 business days
#     * Limit follow-ups to 2-3 maximum
#     """)




























































import streamlit as st
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up Streamlit app
st.set_page_config(page_title="Student Email Assistant", page_icon="✉️", layout="wide")
st.title("✉️ AI-Powered Email & Networking Assistant")
st.markdown("Generate professional emails and messages for academic and career needs.")

# Email Templates
templates = {
    "cold_email": "Write a professional cold email to a recruiter.\n\nCompany: {company}\nPosition: {position}\nRecipient: {recipient}\nBackground: {background}\nKey Points: {key_points}\n\nThe email should be concise and compelling.",
    "linkedin_message": "Write a LinkedIn message for {purpose}.\n\nRecipient: {recipient}\nBackground: {background}\nConnection Context: {connection_context}\nKey Points: {key_points}\n\nKeep it under 300 characters and professional.",
    "academic_email": "Write an email to a {recipient_role}.\n\nRecipient: {recipient}\nPurpose: {purpose}\nCourse Details: {course_details}\nKey Information: {key_information}\n\nThe email should be formal and well-structured.",
    "cover_letter": "Write a cover letter for {position} at {company}.\n\nBackground: {background}\nKey Skills: {key_skills}\nJob Description: {job_description}\n\nThe letter should highlight skills and express interest.",
    "follow_up": "Write a follow-up email about {previous_interaction}.\n\nRecipient: {recipient}\nPrevious Date: {prev_date}\nContext: {context}\nPurpose: {purpose}\n\nThe email should reference prior interaction and include next steps."
}

# Function to generate email using Groq API
def generate_email(email_type, context_data):
    formatted_prompt = templates[email_type].format(**context_data)
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "messages": [
            {"role": "system", "content": "You are a professional email assistant."},
            {"role": "user", "content": formatted_prompt}
        ],
        "model": "llama3-70b-8192",
        "temperature": 0.7,
        "max_tokens": 1000
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error generating email.")

# Sidebar for email type selection
with st.sidebar:
    email_type = st.selectbox("Select Email Type", list(templates.keys()), format_func=lambda x: x.replace("_", " ").title())
    st.header("History")
    if 'history' not in st.session_state:
        st.session_state.history = []
    for i, item in enumerate(st.session_state.history):
        if st.button(f"{item['type']} - {item['date']}", key=f"history_{i}"):
            st.session_state.selected_history = item

# User Input Form
col1, col2 = st.columns([1, 1])
with col1:
    st.header("Input Information")
    with st.form(key="email_form"):
        context_data = {}
        if email_type == "cold_email":
            context_data = {key: st.text_input(key.replace("_", " ").title()) for key in ["company", "position", "recipient", "background", "key_points"]}
        elif email_type == "linkedin_message":
            context_data = {key: st.text_input(key.replace("_", " ").title()) for key in ["purpose", "recipient", "connection_context", "background", "key_points"]}
        elif email_type == "academic_email":
            context_data = {key: st.text_input(key.replace("_", " ").title()) for key in ["recipient_role", "recipient", "purpose", "course_details", "key_information"]}
        elif email_type == "cover_letter":
            context_data = {key: st.text_input(key.replace("_", " ").title()) for key in ["position", "company", "background", "key_skills", "job_description"]}
        elif email_type == "follow_up":
            context_data = {key: st.text_input(key.replace("_", " ").title()) for key in ["previous_interaction", "recipient", "prev_date", "context", "purpose"]}
        submit_button = st.form_submit_button("Generate Email")

# Display Output
with col2:
    st.header("Generated Email")
    if submit_button:
        with st.spinner("Generating email..."):
            generated_email = generate_email(email_type, context_data)
            st.session_state.history.insert(0, {"type": email_type, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "context": context_data, "email": generated_email})
            st.text_area("Your Email", generated_email, height=400)
            st.download_button("Download", generated_email, f"{email_type}_{datetime.now().strftime('%Y%m%d')}.txt", "text/plain")

# Display History
if 'selected_history' in st.session_state:
    st.subheader("Saved Email")
    st.text_area("History", st.session_state.selected_history["email"], height=400)

# Tips Section
st.header("Professional Communication Tips")
tabs = st.tabs(["Email Etiquette", "LinkedIn Messaging", "Follow-up Timing"])
with tabs[0]:
    st.markdown("* Use a professional email address\n* Keep emails concise\n* Proofread before sending")
with tabs[1]:
    st.markdown("* Personalize connection requests\n* Be clear about your purpose\n* Keep it professional and to the point")
with tabs[2]:
    st.markdown("* Follow up on job applications within a week\n* Send thank-you emails after interviews within 24-48 hours")
