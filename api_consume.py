#This an python application that consume an API from https://jsonplaceholder.typicode.com/ 
import requests

#Method that checks if connection is working
def check_connection():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.status_code

#Method to get the user id that matches the email "Nathan@yesenia.net"
def get_user_id(email):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    for user in response.json():
        if user['email'] == email:
            return user['id']


#Method to get the user name that matches the user id "1"
def get_user_name(user_id):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    for user in response.json():
        if user['id'] == user_id:
            return user['name']

#Method to get the posts from a specific user id
def get_posts(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    for post in response.json():
        if post['userId'] == user_id:
            return post['title']

#Mehod to count the amount of albums and photos for a specific user id
def get_albums_photos(user_id):
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    albums = 0
    photos = 0
    for album in response.json():
        if album['userId'] == user_id:
            albums += 1
            id=album['userId']
            url2 = "https://jsonplaceholder.typicode.com/photos"
            responsePh = requests.get(url2)
            for photo in responsePh.json():
                if photo['id'] == id:
                    photos += 1

    return albums, photos

#Method that create an output json with the information of the user in one response
def create_output_json(user_id):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    output = {}
    for user in response.json():
        if user['id'] == user_id:
            output['name'] = user['name']
            output['email'] = user['email']
            output['id'] = user['id']
            output['posts'] = get_posts(user_id)
            output['albums'] = get_albums_photos(user_id)[0]
            output['photos'] = get_albums_photos(user_id)[1]
        
    return output

email="Nathan@yesenia.net"
#get_user_id(email)

print(check_connection())
print(get_user_id(email))
print(get_user_name(3))
print(get_posts(3))
print(get_albums_photos(3))
print(create_output_json(3))


