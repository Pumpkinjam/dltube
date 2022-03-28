import os.path
from pytube import YouTube

class Downloader:
    def __init__(self, path: str = "."):
        self.path = path;
    
    def download(self, link: str, file_type: str = 'mp4', file_name: str = "DEFAULT") -> bool:

        stream = YouTube(link).streams;
        if (file_name == "DEFAULT"):
            file_name = stream[0].title;
        
        if (file_type == 'mp4'):
            video = stream.filter(progressive=True, file_extension=file_type);
            video.get_highest_resolution().download(output_path= self.path, filename= (file_name + '.' + file_type));
        elif (file_type == 'mp3'):
            audio = stream.filter(file_extension=file_type, only_audio=True, subtype='webm', abr='160kbps');
            audio.first().download(output_path= self.path, filename= (file_name + '.' + file_type));
        

        print(f"{file_name}.{file_type}: Download Complete.");
        return True;
        