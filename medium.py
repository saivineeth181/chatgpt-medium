import json
import requests

from chatgpt import generate_text

class medium:
    def __init__(self):
        # Medium API endpoint to create a post
        self.token = "209a7284ef7afc406ae04950e4c46b7f1281ed45484db1f925fe4a41eea13db55"
        self.body = ''
        self.title = ''update.message.text.lower() == 'approved for title'
    
    def run(self):
        user_info = requests.get(f"https://api.medium.com/v1/me?accessToken={token}")
        user_json_info = user_info.json()
        url = f"https://api.medium.com/v1/users/{user_json_info['data']['id']}/posts"
        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        data = {
            "title": str(self.title),
            "contentFormat": "html",
            "content": str(self.body),
            "publishStatus": "draft"
        }

        # make the API request
        response = requests.post(
            url=url,
            headers = headers,
            data = data)
        # check the response status
        if response.status_code == 201:
            return "Post created successfully!"
        else:
            return "Error creating post:" +  str(response.content)
