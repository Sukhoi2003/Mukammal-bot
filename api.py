import requests

API_TOKEN = "3c7bd9ad-2d74-4488-b176-2b1d35a29c0e"





async def api_request(image_url):
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        data={
            'image': image_url,
        },
        headers={'api-key': API_TOKEN}
    )
    data = r.json()


    if data:
        return data["output_url"]

    return None