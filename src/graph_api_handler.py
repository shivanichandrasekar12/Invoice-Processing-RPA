import requests

class GraphAPIHandler:
    def __init__(self, client_id, tenant_id, client_secret):
        self.endpoint = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = ["https://graph.microsoft.com/.default"]

    def get_access_token(self):
        # Logic to get OAuth2 token for secure automation
        data = {
            'client_id': self.client_id,
            'scope': self.scope,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(self.endpoint, data=data)
        return response.json().get('access_token')

    def download_attachments(self, message_id):
        # Logic to download invoice PDFs from Outlook
        print(f"Downloading attachment for message: {message_id}")
        return "data/sample_invoice.pdf"
