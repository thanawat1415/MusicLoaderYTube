import os
import yt_dlp


def search_youtube(title):
    """Search YouTube for a title and return the URL of the top result."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch1',
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{title}", download=False)
    entries = info.get('entries', [])
    if not entries:
        return None
    return entries[0].get('webpage_url') or entries[0].get('url')


def download_as_mp3(video_url, folder_name):
    """Download the audio from a YouTube URL and save it as MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def main():
    choice = input("Enter '1' to input a music title or '2' to use a text file: ")

    if choice == '1':
        title = input("Enter the music title: ")
        music_titles = [title]
    elif choice == '2':
        file_path = os.path.join(os.getcwd(), "music_titles.txt")
        with open(file_path, 'r') as file:
            music_titles = [t for t in file.read().splitlines() if t.strip()]
    else:
        print("Invalid choice. Please try again.")
        return

    folder_name = os.path.join(os.getcwd(), "audio_files")
    os.makedirs(folder_name, exist_ok=True)

    success_count = 0
    fail_count = 0

    for title in music_titles:
        print(f"Downloading: {title}...")
        try:
            video_url = search_youtube(title)
            if not video_url:
                print(f"  No results found for: {title}")
                fail_count += 1
                continue
            download_as_mp3(video_url, folder_name)
            print(f"  Done: {title}")
            success_count += 1
        except Exception as e:
            print(f"  Failed to download '{title}': {e}")
            fail_count += 1

    print(f"\nFinished — {success_count} succeeded, {fail_count} failed.")


if __name__ == "__main__":
    main()

