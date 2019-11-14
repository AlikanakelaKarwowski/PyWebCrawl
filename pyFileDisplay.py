import os

submission_dir = "gitTest"

#create a directory list that may contain files
directory_list = list(os.listdir(submission_dir))

#print out all the different directories and files in submission_dir
def print_List(sub_dir, dir_list):
    for directory in dir_list:
        file_list = list(os.listdir(os.path.join(sub_dir, directory)))
        if len(file_list) != 0:
            file_tup = (directory, file_list)
        print file_tup

#run print_List
print_List(submission_dir,directory_list)
