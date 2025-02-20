import requests, json, csv

def fetch_and_print_posts():
    post = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post.status_code}")
    if post.status_code == 200:
        post_list = post.json()
        for x in post_list:
            print(x['title'])

def fetch_and_save_posts():
    post = requests.get('https://jsonplaceholder.typicode.com/posts')
    if post.status_code == 200:
        post_list = post.json()
        with open("saved_posts", 'w') as f:
            my_keys = ['id', 'title', 'body']
            w = csv.DictWriter(f, fieldnames=my_keys)
            w.writeheader()
            for x in post_list:
                w.writerow({'id': x['id'], 'title': x['title'], 'body': x['body']})
