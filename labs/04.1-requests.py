# Module that interacts with the API created at
# http://andrewbeatty1.pythonanywhere.com/books
# Author: Clare Tubridy

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def read_books(id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    return response.json()

def create_book(book):
    response = requests.post(url, json=book)
    return response

def update_book(id, book):
    put_url = url + "/" + str(id)
    response = requests.put(put_url, json=book)
    return response.json()

def delete_book(id):
    delete_url = url + "/" + str(id)
    response = requests.delete(delete_url)
    return response.json()

if __name__ == "__main__":

    book = {
        'Author':"test",
        'Title':"test title",
        'Price':321
    }

    book_update = {
        'Price':333
    }

    #print(read_books())
    #print(create_book(book))
    #print(update_book(293, book_update))
    print(delete_book(293))