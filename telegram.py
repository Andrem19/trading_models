import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_inform_message(message):
    api_token = os.getenv("API_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.ok:
        print("Inform message sent successfully!")
    else:
        print("Failed to send inform message. Response:", response.text)

# Example usage
# message = "This is an inform message!"

# send_inform_message(message)