from youtube_transcript_api import YouTubeTranscriptApi
import re

video_urls = [
    "https://www.youtube.com/watch?v=Yp03WwNrk9c&t=372s",
    
]

api = YouTubeTranscriptApi()

for url in video_urls:
    try:
        video_id = re.search(r"v=([^&]+)", url).group(1)

        transcript = api.fetch(video_id)

        filename = f"{video_id}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Video Transcript\n\n")
            f.write(f"URL: {url}\n\n")
            f.write("## Transcript\n\n")

            for entry in transcript:
                f.write(entry.text + "\n")

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error with {url}: {e}")