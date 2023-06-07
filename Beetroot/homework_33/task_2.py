import requests
import json

subreddit = 'AskReddit'  # Replace with your desired subreddit
url = f'https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=1000&sort=asc'

comments = []
after = None

while True:
    if after:
        url = f'{url}&after={after}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        comments.extend(data['data'])
        after = data['data'][-1]['created_utc']
        print(f'Downloaded {len(data["data"])} comments. Total comments: {len(comments)}')

        if len(data['data']) < 1000:
            break
    else:
        print(f'Error: {response.status_code}')
        break

output_filename = f'{subreddit}_comments.json'
with open(output_filename, 'w') as file:
    json.dump(comments, file, indent=4)

print(f'Comments saved to {output_filename}')
