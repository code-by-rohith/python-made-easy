import requests

url = "https://api.restful-api.dev/objects/ff80818190a5a11e0190a6cee59603de"

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        print("Data structure:", data)

        if isinstance(data, list) and data:
            first_post = data[0]
            print("Title:", first_post.get('title', 'No title found'))
            print("Body:", first_post.get('body', 'No body found'))
        else:
            print("No data found or data is not a list.")
    except ValueError:
        print("Failed to decode JSON.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
