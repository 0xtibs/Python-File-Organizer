import os
import pyfiglet
from pathlib import Path

ascii_banner = pyfiglet.figlet_format("Alexander's File Organizer")
print(ascii_banner)

DIRECTORIES = {
    "html": [".html5", ".html", ".htm", ".xhtml"],
    "images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "archieves": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "plaintext": [".txt", ".in", ".out"],
    "pdf": [".pdf"],
    "python": [".py"],
    "xml": [".xml"],
    "pkg/exe": [".pkg",".exe"],
    "bash": [".sh"]
  
}
  
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
  
def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
    try:
        os.mkdir("other_Files")
    except ValueError:
        print("failed to create new dir")  
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
  
if __name__ == "__main__":
    organize_junk()
