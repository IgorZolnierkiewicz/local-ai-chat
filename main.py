import requests

url="http://localhost:11434/api/generate"
while(True):

    payload={
        "model": "phi3",
        "prompt": input("Ty: "),
        "stream": False
    }
    response=requests.post(url,json=payload)

    if response.status_code==200:
        data=response.json()
        odpowiedz=data['response']
        print("AI: ", odpowiedz)
    else:
        print("Błąd serwera: ", response.status_code)