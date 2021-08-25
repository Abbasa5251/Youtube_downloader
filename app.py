from pytube import YouTube

def download():
    print("\n\n--------YouTube Video Downloader--------\n\n")

    # Link for Youtube Video
    url = input("Enter Your Youtube URL: ")
    yt = YouTube(url)
    print(f"Title: {yt.title}")
    videos = yt.streams.filter(only_audio=True)
    # Get all Available Youtube Video and Audio Links
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