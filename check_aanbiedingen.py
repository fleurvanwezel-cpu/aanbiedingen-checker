import requests
from bs4 import BeautifulSoup

MERKEN = [
    "nivea",
    "dove",
    "andrelon",
    "rituals"
]

def controleer_kruidvat():
    resultaten = []

    for merk in MERKEN:

        url = f"https://www.kruidvat.nl/search?text={merk}"

        try:
            r = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            if r.status_code == 200:
                resultaten.append(
                    f"Kruidvat gecontroleerd: {merk}"
                )

        except Exception as e:
            resultaten.append(
                f"Fout bij {merk}: {e}"
            )

    return resultaten


if __name__ == "__main__":

    resultaten = controleer_kruidvat()

    print("\n".join(resultaten))
