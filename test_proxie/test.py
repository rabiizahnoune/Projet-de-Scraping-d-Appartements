import requests

# Liste des proxys
proxies_list = [
    "116.125.141.115:80",
    "43.134.121.40:3128",
    "160.86.242.23:8080",
    "144.76.138.69:8888",
    "128.199.79.183:3128",
    "51.91.157.66:80",
    "157.245.27.9:8080",
    "137.184.154.121:443",
    "64.225.8.0:8080",
    "206.189.230.230:443",
    "161.35.70.249:8080",
    "104.248.63.17:30588",
    "68.183.185.62:8080",
    "178.128.211.54:8080",
    "143.198.242.86:443",
    "178.62.65.224:3128",
    "161.35.223.141:8080",
    "206.189.157.23:443",
    "161.35.70.249:80",
    "143.198.242.86:8080"
]


# URL de test
test_url = "http://httpbin.org/ip"

for proxy in proxies_list:
    try:
        # Format du proxy
        proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        
        # Requête de test
        response = requests.get(test_url, proxies=proxy_dict, timeout=5)
        
        # Afficher la réponse si le proxy est fonctionnel
        if response.status_code == 200:
            print(f"Proxy {proxy} est fonctionnel : {response.json()}")
        else:
            print(f"Proxy {proxy} n'a pas pu être utilisé.")
            
    except requests.exceptions.RequestException as e:
        print(f"Erreur avec le proxy {proxy} : {e}")
