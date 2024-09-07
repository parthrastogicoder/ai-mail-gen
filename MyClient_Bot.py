import os
import smtplib
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import pandas as pd
from langchain_groq import ChatGroq
import json

# Load environment variables
load_dotenv()

# Set your API key from the .env file
api_key = os.getenv("GROQ_API_KEY")
email_password = os.getenv("EMAIL_PASSWORD")
from_email = os.getenv("EMAIL_ADDRESS")

# Initialize the ChatGroq model
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

def generate_email_content(name, service):
    prompt = f"""
    You are a professional email writer. Write a personalized email for {name} about our {service} service.
    Highlight how our services in ChatBot Development, RAG (Retrieval Augmented Generation) Development, Python Assignments, and Basic ML tasks can benefit them.
    Ensure the email is professional, engaging, and client-friendly. No Preamble or Signature. No Markdown. No ``` ```
    Format the response with the subject on the first line and the body on subsequent lines.
    """

    messages = [
        ("system", "You are a professional email writer."),
        ("human", prompt)
    ]

    ai_msg = llm.invoke(messages)

    try:
        response_lines = ai_msg.content.strip().split("\n")
        if len(response_lines) < 2:
            raise ValueError("Response does not contain a subject and body.")

        # Ensure no unwanted "Subject:" prefix
        subject = response_lines[0].strip()
        if subject.lower().startswith("subject:"):
            subject = subject[len("subject:"):].strip()

        body = "\n".join(response_lines[1:]).strip()
        return subject, body
    except ValueError as e:
        print(f"Failed to parse response: {e}")
        return None, None

def send_email(to_email, subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, email_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Streamlit UI
st.title("Bulk Email Sender")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    if st.button("Send Emails"):
        for index, row in df.iterrows():
            client_name = row['Name']
            client_email = row['Email']
            client_service = row['Service']

            email_subject, email_body = generate_email_content(client_name, client_service)
            if email_subject and email_body:
                send_email(client_email, email_subject, email_body)
                st.success(f"Email sent to {client_email}")
            else:
                st.error(f"Failed to generate email content for {client_email}")

