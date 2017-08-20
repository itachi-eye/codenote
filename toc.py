import os
import urllib.parse

ignore_dir_or_file = ['.git', 'README.md', 'toc.py', 'code', '.DS_Store', '.gitignore']

GIT_TREE_URL = 'https://github.com/cangsangyuemanlou/codenote/tree/master'
GIT_BLOB_URL = 'https://github.com/cangsangyuemanlou/codenote/blob/master'

root_path = 'E:\\projects\\StudyNote\\codenote'
space_char = '&emsp;'


def go_through_path(basepath, deep=0, parents=''):
    all_files = []

    all_files_list = list(filter(lambda f: f not in ignore_dir_or_file, os.listdir(basepath)))

    dirflt = filter(lambda f: os.path.isdir(os.path.join(basepath, f)), all_files_list)
    for d in dirflt:
        all_files.append(d)

    files = sorted(filter(lambda f: os.path.isfile(os.path.join(basepath, f)), all_files_list),
                   key=lambda f: os.path.getctime(os.path.join(basepath, f)))
    for fl in files:
        all_files.append(fl)

    for file in all_files:
        filepath = os.path.join(basepath, file)
        if os.path.isdir(filepath):
            yield (1, deep, parents, file)  # dir
            yield from go_through_path(filepath, deep + 1, '/'.join([parents, file]))
        else:
            yield (0, deep, parents, file)  # file


def get_git_conent():
    for info in go_through_path(root_path):
        filepath = '/'.join(info[2:])
        filepath = urllib.parse.quote(filepath)
        if info[0] == 1:
            giturl = GIT_TREE_URL + filepath
        else:
            giturl = GIT_BLOB_URL + filepath
        yield (info[1], info[3], giturl)


def write_readme():
    readme_file_path = root_path + '/README.md'
    with open(readme_file_path, 'w', encoding='utf-8') as fp:
        for item in get_git_conent():
            fp.write("{space}[{content}]({link})  \r\n"
                     .format(space=space_char * item[0], content=item[1], link=item[2]))


if __name__ == '__main__':
    root_path = os.path.abspath('.')
    write_readme()
