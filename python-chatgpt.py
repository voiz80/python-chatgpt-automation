import requests
import os
import menu

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

req_data = {
    "model": "text-davinci-003",
    "prompt": f"Hello Chat GPT3. {menu.final_prompt}",
    "max_tokens": 500,
    "temperature": 0.5
}
print(f"Your choice is: {menu.final_prompt} Name of the file: {menu.file_name}")
response = requests.post(api_endpoint, headers=request_headers, json=req_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(menu.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
