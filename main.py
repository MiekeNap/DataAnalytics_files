__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
import shutil
import zipfile
import os.path


directory = './files/cache'
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)


def clean_cache():
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


clean_cache()

my_zip_file = './files/data.zip'
my_cache_dir = './files/cache/'


def cache_zip(path_to_zip_file, cache_dir_path):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)


cache_zip(path_to_zip_file=my_zip_file, cache_dir_path=my_cache_dir)


def cached_files():
    files = []
    dir_path = os.path.abspath(path)
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        files.append(filepath)
    return files


print(cached_files())

file_list = cached_files()


def find_password(file_list):
    for file in file_list:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    passwordline = line
                    break
    return passwordline[10:-1]


print(find_password(file_list))
