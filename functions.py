import requests

def get_page_stats(api_key, user_name):
    url = f"https://tiktok-best-experience.p.rapidapi.com/user/{user_name}/feed"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def get_video_data(api_key, video_id):
    url = f"https://tiktok-best-experience.p.rapidapi.com/video/{video_id}"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    return response.json()
