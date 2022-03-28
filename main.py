import downloader as ydl

dl = ydl.Downloader();



tmp = int(input(
"""Select the file type:
1. mp4
2. mp3
>>> """
));

ftype = 'mp4' if tmp == 1 else 'mp3';

while(True):
    link = input("Input youtube link (input 'quit' for exiting program): ");
    if link == 'quit':
        break;
    
    name = input("Input file name (use '*' for using default name): ");
    if name == '*':
        dl.download(link, ftype);
    else:
        dl.download(link, ftype, name);