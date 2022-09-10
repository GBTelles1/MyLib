import os

def renameLastFile(path, new_name):

    files_list = os.listdir(path)

    dates_list = []

    for file in files_list:
        date = os.path.getmtime(f'{path}\\{file}')
        dates_list.append((date, file))

    dates_list.sort(reverse=True)
    latest_file = dates_list[0][1]
    
    old_file = os.path.join(path, latest_file)
    new_file = os.path.join(path, new_name)
    os.rename(old_file, new_file)

    print(f'The file {latest_file} was renamed to {new_name}.')