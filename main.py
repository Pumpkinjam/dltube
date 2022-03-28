import downloader as ydl

tmp = int(input(
"""Select the file type:
1. mp4
2. mp3
>>> """
));
ftype = 'mp4' if tmp == 1 else 'mp3';

download_dir = input("Input Download Directory (use '/' for default): ");

dl = ydl.Downloader('../dltube/download' if download_dir == '/' else download_dir);

while(True):
    link = input("Input youtube link (input 'quit' for exiting program): ");
    if link == 'quit':
        break;
    
    name = input("Input file name (use '/' for using default name): ");
    if name == '/':
        dl.download(link, ftype);
    else:
        dl.download(link, ftype, name);