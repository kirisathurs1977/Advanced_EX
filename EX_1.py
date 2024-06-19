import requests  # Import the requests module to handle HTTP requests
URL="https://agri.senzmate.com"
page=requests.get(URL)
print(page.text)