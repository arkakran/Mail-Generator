# AI-Powered Email & Networking Assistant for Students

This Streamlit app helps students create professional emails and networking messages for various scenarios.

## Features

- Cold Email Generator for HR recruiters
- LinkedIn Short Message Helper
- Email to College Authorities
- Cover Letter Generator
- Follow-up Email Assistant

## Setup Instructions

Follow these simple steps to get the app running:

### 1. Clone or Download the Files

Make sure you have all these files in your project directory:
- `app.py` (main application)
- `requirements.txt` (dependencies)
- `.env` (for API keys)
- `templates.json` (optional - for template database)

### 2. Set Up Your Environment

1. Install Python 3.7 or higher if you don't have it already
2. Open a terminal/command prompt and navigate to your project directory
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

### 3. Install Dependencies

Run this command to install all required packages:
```
pip install -r requirements.txt
```

### 4. Set Up Your API Key

1. Get an OpenAI API key from [OpenAI's platform](https://platform.openai.com/)
2. Open the `.env` file and replace `your_openai_api_key_here` with your actual API key

### 5. Run the Application

Start the app with this command:
```
streamlit run app.py
```

The app should open automatically in your web browser at http://localhost:8501

## Using the App

1. Select the type of email you want to generate from the sidebar
2. Fill in the required information in the form
3. Click "Generate Email" to create your professional message
4. Copy or download the generated email for your use

## Advanced Configuration

### Using Claude or Groq Instead of OpenAI

To use Claude or Groq AI models instead:

1. Get the appropriate API key (Anthropic for Claude, Groq for Groq)
2. Install the relevant SDK:
   ```
   pip install anthropic  # For Claude
   pip install groq       # For Groq
   ```
3. Modify the `.env` file to include your new API key
4. Edit the `generate_email` function in `app.py` to use the appropriate API

### Adding More Templates

You can expand the template database by editing the `templates.json` file.

## Troubleshooting

- **API errors**: Make sure your API key is correct and you have available credits
- **Installation issues**: Ensure you have the correct Python version and all dependencies installed
- **App not loading**: Check if Streamlit is installed correctly and port 8501 is available

## Next Steps for Enhancement

- Add more email templates and categories
- Implement email saving and exporting to Gmail/Outlook
- Add tone adjustment options for different contexts
- Integrate with LinkedIn API for direct message sending