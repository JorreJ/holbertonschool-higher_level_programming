#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API
    and prints the title of each post.

    It sends a GET request to 'https://jsonplaceholder.typicode.com/posts',
    checks the status code of the response,
    and if the request is successful (status code 200),
    it prints the title of each post.
    """
    post = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post.status_code}")
    if post.status_code == 200:
        post_list = post.json()
        for x in post_list:
            print(x['title'])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    It sends a GET request to 'https://jsonplaceholder.typicode.com/posts',
    checks the status code of the response,
    and if the request is successful (status code 200),
    it saves the post data (id, title, and body)
    into a CSV file called 'saved_posts'.
    """
    post = requests.get('https://jsonplaceholder.typicode.com/posts')
    if post.status_code == 200:
        post_list = post.json()
        with open("saved_posts", 'w', newline='', encoding='utf-8') as f:
            # Define the field names for the CSV file
            my_keys = ['id', 'title', 'body']
            # Create a CSV DictWriter object to write data in dictionary form
            w = csv.DictWriter(f, fieldnames=my_keys)
            # Write the header row (field names) to the CSV file
            w.writeheader()
            for x in post_list:
                # Write each post data as a row in the CSV file
                w.writerow({'id': x['id'],
                            'title': x['title'],
                            'body': x['body']})
            print("Posts saved in saved_posts")
    else:
        print("Failed to fetch posts")
