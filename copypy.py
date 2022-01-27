import os
import sys
import shutil
import math




# Terminal flags and arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-sb", "--subdirs", dest='subdirst', action='store_true', help="Copy With Subdirs.")
parser.add_argument("-f", "--from", dest = "from_dir", help="Get Files From Directory.", required=True)
parser.add_argument("-t", "--to", dest = "to_dir", help="Copy Files To Directory.", required=True)
args = parser.parse_args()







def CountFiles(from_dir):
    files_number = 0
    for root, subdirs, files in os.walk(from_dir):
        for file in files:
            files_number += 1
    return files_number



def CopyOnlyFiles(from_dir, to_dir, files_number):
    not_deleted = []
    counter = 0
    for root, subdirs, files in os.walk(from_dir):
        for file in files:
            from_path = root + "\\" + file
            to_path = to_dir + "\\" + file
            to_path = to_path.replace(" ", "_")
            if not os.path.exists(to_path):
                shutil.copy(from_path, to_path)
            if not os.path.exists(to_path):
                not_deleted.append(from_path)
            counter += 1
            percent = round((counter*100)/files_number)
            print("%d %%" % percent, end='\r')
    return not_deleted



def CopyWithSubDirs(from_dir, to_dir, files_number):
    not_deleted = []
    counter = 0
    for root, subdirs, files in os.walk(from_dir):
        for file in files:
            to_directory = root.replace(from_dir, to_dir)
            to_directory = to_directory.replace(" ", "_")
            if not os.path.exists(to_directory):
                os.makedirs(to_directory)
            from_path = root + '\\' + file
            to_path = to_directory + "\\" + file
            to_path = to_path.replace(" ", "_")
            if not os.path.exists(to_path):
                shutil.copy(from_path, to_path)
            if not os.path.exists(to_path):
                not_deleted.append(from_path)
            counter += 1
            percent = round((counter*100)/files_number)
            print("%d %%" % percent, end='\r')
    return not_deleted
            






if __name__ == "__main__":
    from_dir = args.from_dir
    to_dir = args.to_dir
    subdirs = args.subdirst
    files_number = CountFiles(from_dir)
    if subdirs:
        not_deleted_files = CopyWithSubDirs(from_dir, to_dir, files_number)
    else:
        not_deleted_files = CopyOnlyFiles(from_dir, to_dir, files_number)
    print("Can't Delete This Files: %d" % len(not_deleted_files))
    for file in not_deleted_files:
        print(file)
