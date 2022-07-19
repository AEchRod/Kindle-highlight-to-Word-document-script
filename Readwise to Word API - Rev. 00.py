import requests
from docx import Document
#import datetime

document = Document()

#getting books that were updated last week, if needed:
#a_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)

querystring_category = {
    "category": "books",
}

#To check if GET request works
response_auth = requests.get(
    url="https://readwise.io/api/v2/auth/",
    headers={"Authorization": "Token xxx"}
)

response_books = requests.get(
    url="https://readwise.io/api/v2/books/",
    headers={"Authorization": "Token xxx"},
    params=querystring_category
)

#this variable contains the whole booklist
data_booklist = response_books.json()

#this variable contains only the results from the booklist
booklist_results = data_booklist["results"]

x = [book["id"] for book in booklist_results]

for id in x:
    querystring_bookid = {
        "book_id": id,
    }
    #this query string selects books individually


    #this requests gets the highlist list
    response = requests.get(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": "Token xxx"},
            params=querystring_bookid
        )

    #this retrieves a json from the highlist list
    data_highlights = response.json()

    highlight_results = data_highlights["results"]

    for highlight in highlight_results:
        document.add_paragraph(highlight["text"])
    document.save('Highlights.docx')



