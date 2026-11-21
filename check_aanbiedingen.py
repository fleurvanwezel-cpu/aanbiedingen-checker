import requests

url = "https://api.kruidvat.nl/api/v2/kvn-spa/search?fields=FULL&searchType=PRODUCT&query=nivea&lang=nl&curr=EUR"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("Content-Type"))
print("Eerste 1000 tekens:")
print(r.text[:1000])
