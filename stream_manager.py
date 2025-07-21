import yt_dlp
#import time
import vlc

ydl_opts = {'quiet': True, 'no warnings': True}

def play_stream(selected_stream: str):
    """
    playing the stream using mpv, the input should be a string url
    """
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        info = ydl.extract_info(selected_stream, download=False)
        url = info["url"]
    
    #creating our player object with these settings
    instance_args = ['--no-video', '--quiet']
    instance = vlc.Instance(instance_args)
    player = instance.media_player_new(url)
    player.play()
    
    return player

        
