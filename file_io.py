import os


# Creates a Reading List project/directory

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
    else:
        pass


# Creates a new file

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Within a website (project/directory), create a reading_list file

def create_data_file(project_name, content):
    # Creates a path (reading_list)
    reading_list = project_name + '/reading_list.txt'
    if not os.path.isfile(reading_list):
        # If there is no reading_list file - write/create a reading_list file with the content in it
        write_file(reading_list, content)


# Add data to an existing file

def append_to_file(path, data):
    # with as - opens the file and as soon as I exit the block(execute everything in it) it automatically closes
    with open(path, 'a') as file:
        file.write(data + '\n' + '\n')


# Delete the contents of a file

def delete_file_content(path):
    with open(path, 'w'):
        # Does nothing/writes nothing, creates a new file with the same name/overwrites
        pass


# Read a file and convert each line to set element

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line in the file

def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)


