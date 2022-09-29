__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
import shutil
import zipfile
import os.path


cache_dir = 'cache'
my_zipfile = 'data.zip'
parent_dir = os.getcwd()
path_to_cache = os.path.join(parent_dir, cache_dir)
path_to_zipfile = os.path.join(parent_dir, my_zipfile)


def clean_cache():
    if os.path.exists(path_to_cache):
        shutil.rmtree(path_to_cache)
        os.mkdir(path_to_cache)
    else:
        os.mkdir(path_to_cache)


def cache_zip(path_to_zipfile, path_to_cache):
    with zipfile.ZipFile(path_to_zipfile, 'r') as zip_ref:
        zip_ref.extractall(path_to_cache)


def cached_files():
    files = []
    dir_path = os.path.abspath(path_to_cache)
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        files.append(filepath)
    return files


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


if __name__ == '__main__':
    clean_cache()
    cache_zip(path_to_zipfile, path_to_cache)
    print(cached_files())
    print(find_password(file_list))
