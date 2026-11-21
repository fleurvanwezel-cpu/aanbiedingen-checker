import requests

merken = [
    "nivea",
    "dove",
    "rituals",
    "andrelon"
]

for merk in merken:

    url = (
        "https://api.kruidvat.nl/api/v2/kvn-spa/search"
        f"?fields=FULL&searchType=PRODUCT&query={merk}"
        "&lang=nl&curr=EUR"
    )

    data = requests.get(url).json()

    for product in data["products"]:

        if product.get("topPromotion"):

            print(
                product["name"],
                "-",
                product["price"]["formattedValue"],
                "-",
                product["topPromotion"]["title"]
            )
