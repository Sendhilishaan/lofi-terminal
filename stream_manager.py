from yt_dlp import YoutubeDL 
import yt_dlp
import subprocess

mpv_exe = r"D:\mpv-x86_64-20250713-git-bd21180\mpv.exe"
ydl_opts = {'quiet': True, 'no warnings': True}

def play_stream(selected_stream: str):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        info = ydl.extract_info(selected_stream, download=False)
        url = info["url"]
        print("Stream URL obtained successfully!")

        # Running the mpv subprocess
        subprocess.run([mpv_exe,'--no-video',url], stdout=subprocess.DEVNULL)