import yt_dlp
import subprocess
from menu import loading

mpv_exe = r"D:\mpv-x86_64-20250713-git-bd21180\mpv.exe"
ydl_opts = {'quiet': True, 'no warnings': True}

def play_stream(selected_stream: str):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        info = ydl.extract_info(selected_stream, download=False)
        url = info["url"]
        
        loading()
        subprocess.run([mpv_exe,'--no-video', url]) #stdout=subprocess.DEVNULL to hide mpv