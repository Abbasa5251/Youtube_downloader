from pytube import YouTube
from pytube import Playlist

def download():
    print("\n\n--------YouTube Video Downloader--------\n\n")

    # Link for Youtube Video
    url = input("Enter Your Youtube URL: ")

    choice = input("Do you want to download playlist? (y/n): ")
    if choice.lower() == "y":
        yt = Playlist(url)
        print(f'Playlist Name: {yt.title}')
        print("Downloading...")
        for i, stream in enumerate(yt.videos):
            # print(f"{str(i)} {str(stream.title)}")
            print(stream.streams.get_by_itag(22).title)
            stream.streams.get_by_itag(22).download()
        print("\nDownload complete.")
    else:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        videos = yt.streams.filter(only_audio=True)

        for i, stream in enumerate(videos):
            print(f"{str(i)} {str(stream)}")

        num = int(input("\nEnter Your Choice: "))
        video = videos[num]
        print("Downloading...")
        # Download the Specific Link in Specific Path
        video.download()
        print("\nDownload Complete.")

if __name__=='__main__':
    # Function Call
    download()