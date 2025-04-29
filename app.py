import streamlit as st
import requests
from datetime import datetime

# ✅ Replace with your working API key
GROQ_API_KEY = "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"

# Streamlit app setup
st.set_page_config(page_title="Student Email Assistant", page_icon="✉️", layout="wide")
st.title("✉️ AI-Powered Email & Networking Assistant")
st.markdown("Generate professional emails and messages for academic and career needs.")

# ✅ Test API Key button
if st.button("🔍 Test API Key"):
    test_payload = {
        "messages": [
            {"role": "user", "content": "Say hi"},
        ],
        "model": "llama3-8b-8192",
        "temperature": 0.5,
        "max_tokens": 10
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    test_res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=test_payload)
    if test_res.status_code == 200:
        st.success("✅ API Key is working!")
    else:
        st.error(f"❌ API Key Error: {test_res.status_code} - {test_res.text}")

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
    try:
        formatted_prompt = templates[email_type].format(**context_data)
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
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

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"

# Sidebar for selecting email type and viewing history
with st.sidebar:
    email_type = st.selectbox("Select Email Type", list(templates.keys()), format_func=lambda x: x.replace("_", " ").title())
    st.header("History")
    if 'history' not in st.session_state:
        st.session_state.history = []
    for i, item in enumerate(st.session_state.history):
        if st.button(f"{item['type']} - {item['date']}", key=f"history_{i}"):
            st.session_state.selected_history = item

# Input form
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

# Output section
with col2:
    st.header("Generated Email")
    if submit_button:
        with st.spinner("Generating email..."):
            generated_email = generate_email(email_type, context_data)
            st.session_state.history.insert(0, {
                "type": email_type,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "context": context_data,
                "email": generated_email
            })
            st.text_area("Your Email", generated_email, height=400)
            st.download_button("Download", generated_email, f"{email_type}_{datetime.now().strftime('%Y%m%d')}.txt", "text/plain")

# Show selected history
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
