import os
import shutil
import argparse

def create_file(file):
    if (os.path.isdir(file) == False):
        os.mkdir(file)

def main():
    parser = argparse.ArgumentParser(
        prog="File Organizer",
        description="Organizes the directory into several folders"
    )
    parser.add_argument('-d', '--directory', help='The starting directory you want to organize', default=".")
    args = parser.parse_args()
    directory = str(args.directory)

    file_extensions = {
        'pdf' : 'PDFs',
        'png' : 'Images',
        'PNG' : 'Images',
        'jpg' : 'Images',
        'JPG' : 'Images',
        'jpeg': 'Images',
        'JPEG': 'Images',
        'doc' : 'Documents',
        'docx': 'Documents',
        'txt' : 'Documents',
        'csv' : 'Data',
        'xlsx': 'Data',
        'tsv' : 'Data',
        'zip' : 'Archives',
        'rar' : 'Archives',
        '7z'  : 'Archives',
        'exe' : 'Executables',
        'wav' : 'Music',
        'mp3' : 'Music',
        'mp4' : 'Videos',
        'avi' : 'Videos',
        'fiv' : 'Videos',
        'wmv' : 'Videos',
        'py'  : 'Scripts'
    }

    organized_dir = directory

    create_file(organized_dir)

    os.chdir(directory)
    for file in os.listdir(directory):
        found = False

        if os.path.isdir(file) == True:
            continue
        elif os.path.isfile(file) == True:
            for extension, folder_name in file_extensions.items():
                old_dir = os.path.join(directory, file)
                if (file.endswith("."+extension)):
                    create_file(os.path.join(organized_dir, folder_name))
                    new_dir = os.path.join(organized_dir, folder_name, file)
                    shutil.move(old_dir, new_dir)
                    found = True
                    break
            if found == False:
                create_file(os.path.join(directory, "Others"))
                new_dir = os.path.join(organized_dir, "Others", file)
                shutil.move(old_dir, new_dir)

main()
