# Bulk Email Sender with Personalized Content

This project is a bulk email sender built using Streamlit and LangChain's `ChatGroq` model to generate personalized emails for each recipient. The emails are customized based on the client's name and the services they offer, such as E-commerce, Digital Marketing, etc. This project supports reading data from a CSV file and sending emails using Gmail.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Sample CSV Format](#sample-csv-format)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Personalized email generation using LangChain's ChatGroq model
- Bulk email sending using Gmail's SMTP
- CSV file input for client data (Name, Email, Service)
- Real-time feedback through a web interface powered by Streamlit

## Requirements

- Python 3.8+
- A valid Gmail account with [App Password](https://support.google.com/accounts/answer/185833?hl=en)
- API Key from Groq for `ChatGroq` integration

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/codebytemirza/MY-CLIENT-BOT-AI-MAIL-SENDER.git
   cd MY-CLIENT-BOT-AI-MAIL-SENDER
   ```

2. **Create a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Packages**

   Install all the necessary dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   You need to create a `.env` file for your API key and email credentials. In the project root directory, create a `.env` file:

   ```bash
   touch .env
   ```

   Add the following content to `.env`:

   ```bash
   GROQ_API_KEY=your_api_key
   EMAIL_PASSWORD=your_app_specific_password
   EMAIL_ADDRESS=your_gmail_address@gmail.com
   ```

   - Replace `your_app_specific_password` with your Gmail app-specific password.
   - Replace `your_gmail_address@gmail.com` with your Gmail address.

5. **Run the Application**

   Start the Streamlit app by running:

   ```bash
   streamlit run app.py
   ```

   This will open a browser window with the Streamlit interface.

## Environment Variables

This project requires the following environment variables to function:

- `GROQ_API_KEY`: Your Groq API key for using `ChatGroq` to generate personalized email content.
- `EMAIL_PASSWORD`: Your Gmail app-specific password to send emails.
- `EMAIL_ADDRESS`: Your Gmail address for sending emails.

The `.env` file should look like this:

```plaintext
GROQ_API_KEY=your_groq_api_key
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_ADDRESS=your_gmail_address
```

## Usage

1. **Upload CSV File**: The app requires a CSV file as input. The CSV file should contain the following columns:

   - `Name`: The name of the client.
   - `Email`: The email address of the client.
   - `Service`: The service you are offering to the client.

2. **Generate Emails**: Once the CSV is uploaded, click the **Send Emails** button to generate and send personalized emails to each client.

3. **Success and Error Messages**: You will get real-time feedback if the email was sent successfully or if there was an error.

## Sample CSV Format

Your CSV file should be in the following format:

```csv
Name,Email,Service
Ecommerce by Experts,ecommercebyexperts@gmail.com,E-commerce
Seordev Digital Marketing Agency,seordev@gmail.com,Digital Marketing
Ubuntu Education Consultancy,ubuntueducation@gmail.com,Education Consultancy
```

## Project Structure

```
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies list
├── .env                # Environment variables (GROQ_API_KEY, EMAIL_PASSWORD, EMAIL_ADDRESS)
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Added feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

---

## How to Obtain a Groq API Key

To get a **Groq API key**, follow these steps:

1. **Sign Up or Log In** to the [Groq Developer Portal](https://console.groq.com/keys).
2. Go to the **API Keys** section and click **Create New API Key**.
3. Copy the generated API key and store it securely.
4. Add it to your `.env` file as shown below:

   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
