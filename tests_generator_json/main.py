import os
import json

# GLOBAL SCRIPT VARS
autogenerated_text = '# autogenerated from test-generator\n'
unit_test_template = 'from django.test import TestCase\n' \
                     'from django.urls import reverse\n' \
                     '\n\n' \
                     'class UnitTest(TestCase):\n'
filename = "test_urls.json"


# Functions
def get_list_of_files(dirname='/', url_filename=filename):
    file_url_list = []

    if os.path.exists(os.path.join(dirname)):
        for root, dir, files in os.walk(dirname, topdown=False):
            for name in files:
                filepath = os.path.join(root, name)
                if url_filename in filepath:
                    file_url_list.append(filepath)
    return file_url_list


# Classes
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


if __name__ == '__main__':

    file_list = get_list_of_files()

    # print list of files
    print("Found {} files.".format(len(file_list)))
    for file in file_list:
        print(file)

    # open file and generate test cases
    for file in file_list:
        print("#######################################################################################################")
        print("Parsing file: '{}'.".format(file))
        print("#######################################################################################################")

        # folder path without the filename
        file_folder_path = file.split(file.split("/")[-1])[0]
        test_folder_path = file_folder_path + "test/"
        test_module_folder_path = file_folder_path + "test/__init__.py"
        test_view_path = test_folder_path + "test_view.py"

        print(file_folder_path)
        print(test_folder_path)

        # create test folder
        if not os.path.exists(test_folder_path):
            os.makedirs(test_folder_path)

        # create __init__.py file if not exist
        if not os.path.exists(test_module_folder_path):
            raw_file = open(test_module_folder_path, 'w')
            raw_file.write("# test-generator autogenerated init file\n")
            raw_file.close()

        # create the autogenerated test code
        with open(file, 'r+') as open_file:
            data = json.load(open_file)

            print(data)

            consent = False
            if not os.path.exists(test_view_path):
                consent = True
            else:
                user_answer = input("File already generated, overwrite? [y/N]  ")
                if user_answer.capitalize() == "Y":
                    consent = True

            if consent:
                with open(test_view_path, 'w') as test_view:
                    test_view.write(autogenerated_text)
                    test_view.write(unit_test_template)

                    for url in data['urls']:
                        req = 'get'
                        request_type = '_' + req.upper()
                        if 'type' in url.keys():
                            request_type = '_' + str(url['type']).upper()
                            req = str(url['type']).lower()

                        if 'name' in url.keys():
                            test_view.write('\n\tdef test_' + url['name'] + request_type + "(self):\n")

                            if 'description' in url.keys():
                                test_view.write('\t\t"""' + url['description'] + '"""\n\n')
                            else:
                                test_view.write('\t\t"""Autogenerated docstring"""\n\n')

                            if 'url' not in url.keys():
                                if 'data' in url.keys():
                                    test_view.write('\t\tresponse = self.client.' + req + '(reverse(\'' + url['name'] +
                                                    '\'), ' + str(url['data']) + ')\n')
                                else:
                                    test_view.write('\t\tresponse = self.client.' + req + '(reverse(\'' + url['name'] +
                                                    '\'))\n')
                            else:
                                if 'data' in url.keys():
                                    test_view.write('\t\tresponse = self.client.' + req + '(\'' + url['url'] + '\',' +
                                                    str(url['data']) + ')\n')
                                else:
                                    test_view.write('\t\tresponse = self.client.' + req + '(\'' + url['url'] + '\')\n')

                            if 'code' in url.keys():
                                test_view.write('\t\tself.assertEqual(response.status_code, ' + url['code'] + ')\n')
                            else:
                                test_view.write('\t\tself.assertEqual(response.status_code, 200)\n')

                            if 'template' in url.keys():
                                test_view.write('\t\tself.assertTemplateUsed(response, \'' + url["template"] + '\')\n')

                            if 'contain' in url.keys():
                                test_view.write('\t\tself.assertContains(response, \'' + url['contain'] + '\')\n')
            else:
                print('Not going to overwrite the current tests.')