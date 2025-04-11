
# AI Generated Email Sender



## Overview

This is a full-stack application that demonstrates rapid prototyping of an AI-powered email sender. The main features of the app include:

- **Recipient Input:** Manually enter one or more email addresses to which the email should be sent.  
- **Prompt Input:** Provide a prompt or context for the email.  
- **Email Generation:** Click on “Generate Email” to let the integrated AI create an email draft based on the provided prompt.  
- **Editable Draft:** Review and modify the AI-generated email draft as needed.  
- **Email Dispatch:** Once satisfied with the edits, send the email to the specified recipients.

The focus of this project is on implementing the core functionalities quickly and efficiently with a basic user interface.

---

## Table of Contents

1. [Approach & Process](#approach--process)
2. [Tech Stack & Rationale](#tech-stack--rationale)
3. [Features](#features)
4. [Requirements](#requirements)
5. [Local Setup](#local-setup)
6. [Environment Variables](#environment-variables)
7. [Usage](#usage)
8. [Deployment](#deployment)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)

---

## 1. Approach & Process

Given the limited timeframe (1.5 hours), the approach is to quickly set up a working MVP with the following process:

- **Rapid Prototyping:** Use tools that allow quick deployment of a web application with minimal UI overhead.
- **Integrating AI:** Leverage an AI service (e.g., LangChain’s ChatGroq or any other AI provider) to generate the email content based on a user prompt.
- **Editable Content:** Ensure the generated email is presented in a text area that can be edited before final sending.
- **Email Dispatch:** Implement a simple email-sending function using a provider such as Gmail via SMTP.

---

## 2. Tech Stack & Rationale

- **Python 3.8+:** Offers a rich ecosystem and rapid development capabilities.
- **Streamlit:** Chosen for its simplicity and speed in creating web interfaces, ideal for prototyping.
- **AI Service Integration:** Utilizes LangChain’s ChatGroq (or an equivalent service) to generate emails from user prompts.
- **Gmail SMTP:** Configured for sending emails, making the integration straightforward and secure with Gmail App Passwords.

---

## 3. Features

- **Manual Recipient Input:** Users can type in the recipient email addresses.
- **Prompt-Based Email Generation:** A prompt input triggers the AI to create an email draft.
- **Editable Drafts:** The generated email can be tweaked in a text area.
- **Direct Email Sending:** Once edits are complete, the user can send the email to the entered recipient(s).

---

## 4. Requirements

- **Python 3.8+**
- A **Gmail account** with an [App Password](https://support.google.com/accounts/answer/185833?hl=en) (recommended if using Gmail SMTP)
- **API Key for AI Service:** For example, a Groq API key if using LangChain’s ChatGroq or a key for any alternative AI service

---

## 5. Local Setup

1. **Clone the Repository**  
   ```bash
   git clone GIT NAME
  
   ```

2. **Create a Virtual Environment (Optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**  
   Create a `.env` file in the project root containing:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   EMAIL_PASSWORD=your_gmail_app_password
   EMAIL_ADDRESS=your_gmail_address
   ```
   - Replace placeholders with your actual values.

5. **Run the Application**  
   ```bash
   streamlit run app.py
   ```
   This command will launch the Streamlit app in your default web browser.

---

## 6. Environment Variables

Ensure that you have the following environment variables configured in your `.env` file:

- `GROQ_API_KEY` – Your AI service API key (e.g., LangChain’s ChatGroq)
- `EMAIL_PASSWORD` – Your Gmail App Password (or password for your chosen email service)
- `EMAIL_ADDRESS` – The email address from which the emails will be sent

---

## 7. Usage

1. **Input Recipients:**  
   Enter one or more recipient email addresses in the designated input field.

2. **Input Email Prompt:**  
   Type a prompt that the AI will use to generate the email.

3. **Generate Email:**  
   Click on the "Generate Email" button. The integrated AI service will create a draft based on your prompt.

4. **Edit the Email:**  
   The generated email will appear in an editable text area. Make any necessary modifications.

5. **Send Email:**  
   Once the email draft is finalized, click the "Send Email" button to dispatch the email to your specified recipients.

---

## 8. Deployment

You can deploy this application using platforms such as:

- **Streamlit Cloud:**  
  1. Push your code to a public GitHub repository.
  2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud).
  3. Follow the instructions to deploy your app directly from your repository.

- **Heroku:**  
  1. Create a `Procfile` with the following content:
     ```plaintext
     web: streamlit run app.py 
     ```
  2. Push your changes to Heroku and set your environment variables in the dashboard.

---

## 9. Project Structure

```
├── app.py                # Main Streamlit application
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables (not tracked by Git)
├── README.md             # Project documentation
└── ...
```

---

## 10. Contributing

Contributions are welcome!

1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request for review.




---

