import requests

def client1():
    url = "http://localhost:8000/upload"
    files = {
        "file": ("example.txt", open("example.txt", "rb")),
    }
    data = {
        "description": "Sample file upload via FastAPI"
    }

    response = requests.post(url, files=files, data=data)
    print(response.json())

def client2():
    """
    Sets Content-Type: multipart/form-data automatically.
    Sends a file and a text field (description) in the same request.
    """
    url = "http://localhost:8000/upload"
    files = {
        'file': ('example.txt', open('example.txt', 'rb')),
        'description': (None, 'Sample file upload')
    }

    response = requests.post(url, files=files)
    print(response.status_code)

# ============================

def client3_download():
    url = "http://localhost:8000/download"
    response = requests.get(url)

    with open("local_copy.txt", "wb") as f:
        f.write(response.content)

    print("Downloaded!")

# ============================

if '__name__' == '__main__':
    client1()
    client2()