
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            #print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
        print('\n')
        print('*' * 70)
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']}")
        print('\n')
        print('*' * 70)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name' : name, 'time' : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update: '))
    if 1 <= index <= len(videos):
        name = input('Enter the new video name: ')
        time = input('Enter the new video time: ')
        videos[index-1] = {'name' : name, 'time' : time}
        save_data_helper(videos)
    else:
        print('Invalid index selected')

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to be deleted: '))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid Video index selected')

def main():
    videos = load_data()
    while True:
        print('\n YOUTUBE MANAGER | CHHOSE AN OPTION')
        print('1. LIST ALL YOUTUBE VIDEOS')
        print('2. ADD A YOUTUBE VIDEO')
        print('3. UPDATE A YOUTUBE VIDEO DETAIL')
        print('4. DELETE A YOUTUBE VIDEO')
        print('5. EXIT THE APP')
        choice = input('ENTER A CHOICE: ')
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _:
                print('Invalid Choice⚠️')

if __name__  == '__main__':
    main()


    