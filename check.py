import requests

# 🔑 Paste your API key here directly (for testing only — don't expose it in production)
GROQ_API_KEY = "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"
def check_groq_api(api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello"}
        ],
        "temperature": 0.5,
        "max_tokens": 50
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("✅ API key is working!")
        print("Response:", response.json()['choices'][0]['message']['content'])
    else:
        print("❌ API key check failed.")
        print("Status Code:", response.status_code)
        print("Error:", response.text)

if __name__ == "__main__":
    check_groq_api(GROQ_API_KEY)
