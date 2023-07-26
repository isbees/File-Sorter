import os
import shutil

# path to the folder you want to sort
# make the user your user name for your computer 
user = ''
path = 'C:/Users/'+user+'/Downloads'

# folders and their types
videos = ['mp4', 'mov', 'wmv', 'webm', 'mkv', 'srt', 'm3u8']
audio = ['mp3','wav','mid','ogg']
images = ['heic', 'pxz', 'pxd', 'jfif', 'webp',  'png', 'jpeg', 'jpg', 'gif', 'ai', 'tiff', 'psd', 'indd', 'raw']
compressed = ['zip', 'tar', 'tgz', 'rar', 'gz', '7z', 'wim', 'xz', 'bzip2', 'gzip']
executables = ['dll', 'exe', 'bat', 'com', 'cmd', 'inf', 'ipa', 'osx', 'pif', 'run', 'wsh', 'msi']
documents = ['opj', 'bak', 'log', 'odt', 'djvu', 'epub', 'pdf', 'doc', 'docx', 'ppt', 'pptx', 'txt', 'm', 'opju', 'xlsx']
code = ['l','scm', 'asc', 'pl', 'json', 'apk', 'sql', 'y', 'i', 'hs', 'c', 'cpp', 'py', 'h', 'jar', 'iqblocks', 'iqpython', 'js', '6', '0', '2', '3']
windows = ['ttf', 'diagcab', 'dat', 'ris', 'lnk', 'ics', '1-rarbg']


list_ = os.listdir(path)

for file_ in list_:
    name, ext = os.path.splitext(file_)
    type_ = ext

    # This is going to store the extension type
    ext = ext[1:]
  
    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue
    
    # Identifies the file types and sorts into a category
    # Could be made simpler with a dictionary but would be unefficent 
    temp = ext.lower()
    if temp in videos:
        ext = 'videos'
    elif temp in audio:
        ext = 'audio'
    elif temp in images:
        ext = 'images'
    elif temp in compressed:
        ext = 'compressed'
    elif temp in executables:
        ext = 'executables'
    elif temp in documents:
        ext = 'documents'
    elif temp in code:
        ext = 'code'
    elif temp in windows:
        ext = 'windows'
    else:
        ext = 'other'

    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
  
    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
