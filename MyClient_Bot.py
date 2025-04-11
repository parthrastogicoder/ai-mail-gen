import os
import smtplib
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Environment variables for the AI and email credentials
api_key = st.secrets["env"]["GROQ_API_KEY"]
email_password = st.secrets["env"]["EMAIL_PASSWORD"]
from_email =st.secrets["env"]["EMAIL_ADDRESS"]

# Initialize the ChatGroq model
llm = ChatGroq(
    api_key=api_key,
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

def generate_email_content(user_prompt):
    """
    This function sends the user prompt to the ChatGroq model to generate 
    an email consisting of a subject and body.
    """
    messages = [
        ("system", "You are a professional email writer."),
        ("human", user_prompt)
    ]

    ai_msg = llm.invoke(messages)

    try:
        response_lines = ai_msg.content.strip().split("\n")
        if len(response_lines) < 2:
            raise ValueError("Response does not contain a subject and body.")
        # Remove any “Subject:” prefix if it exists
        subject = response_lines[0].strip()
        if subject.lower().startswith("subject:"):
            subject = subject[len("subject:"):].strip()
        body = "\n".join(response_lines[1:]).strip()
        return subject, body
    except Exception as e:
        st.error(f"Failed to parse generated email content: {e}")
        return None, None

def send_email(to_email, subject, body):
    """
    This function creates a MIME email and sends it using Gmail's SMTP server.
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, email_password)
        server.sendmail(from_email, to_email, msg.as_string())
        st.info(f"Email sent to {to_email}")
    except Exception as e:
        st.error(f"Failed to send email to {to_email}: {e}")
    finally:
        server.quit()

# Streamlit User Interface
st.title("AI-Generated Email Sender")

# Step 1: Input Recipient(s)
recipients_input = st.text_input(
    "Enter recipient email addresses (comma separated):",
    placeholder="e.g., user1@example.com, user2@example.com"
)

# Step 2: Input Prompt for Email Generation
prompt_input = st.text_area(
    "Enter your prompt for the email generation:",
    placeholder="For example, write a professional email about our new service offering..."
)

# Button to generate email content using AI
if st.button("Generate Email"):
    if not prompt_input:
        st.warning("Please enter a prompt for the email.")
    else:
        subject, body = generate_email_content(prompt_input)
        if subject and body:
            st.session_state["generated_subject"] = subject
            st.session_state["generated_body"] = body
            st.success("Email generated! You can now edit the subject and body below.")

# Step 3: Display editable fields for the generated email
default_subject = st.session_state.get("generated_subject", "")
email_subject = st.text_input("Email Subject", default_subject)
default_body = st.session_state.get("generated_body", "")
email_body = st.text_area("Email Body", default_body, height=300)

# Step 4: Send Email to the Recipients
if st.button("Send Email"):
    if not recipients_input:
        st.warning("Please enter at least one recipient email address.")
    elif not email_subject or not email_body:
        st.warning("Email subject and body cannot be empty.")
    else:
        # Split the input into a list of recipient email addresses
        recipients = [email.strip() for email in recipients_input.split(",") if email.strip()]
        for recipient in recipients:
            send_email(recipient, email_subject, email_body)
        st.success("Email sent successfully to all recipients!")
