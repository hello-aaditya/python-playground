import requests

def fetch_youtuber_info():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos/EQwmQLU1S6I"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        owner = data['data']
        channel_creator = owner['channel']['info']['title']
        subscriber_count = owner['channel']['statistics']['subscriberCount']
        return channel_creator, subscriber_count
    
    else:
        raise Exception ('failed to fetch user data')
    
def main():
    try:
        channel_creator, subscriber_count = fetch_youtuber_info()
        print(f"Youtuber: {channel_creator}\nSubscriber Count: {subscriber_count}")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()