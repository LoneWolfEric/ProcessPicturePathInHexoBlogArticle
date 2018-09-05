import os
import re

class Article:

    def __init__(self, name):
        self.name = name
        self.dir = name.strip('.md')
        print(self.name)
        print(self.dir)

    def run(self):
        f = open(self.name, 'r', encoding='UTF-8')
        f_new = open(self.name + '.new', 'w', encoding='UTF-8')

        lines = f.readlines()
        for line in lines:
            picture_path = re.findall(r'!\[.{0,100}\]\(.{0,10000}\)', line)
            print(line)
            # if not line:
            #     print('none')
            if picture_path:
                picture_path = picture_path[0]
                # print(picture_path)
                new_path = picture_path[0 : picture_path.index('(') + 1] + picture_path[picture_path.index(self.dir) : ] + '\r\n'
                #print(new_path)
                f_new.write(new_path)
            else:
                f_new.write(line)
        f.close()
        f_new.close()

def main():
    article_list = []
    dir_list = []
    article_with_picture_list = []
    files = os.listdir('.')
    # print(files)
    for f in files:
        if '.md' in f:
            article_list.append(f)
        elif '.' not in f:
            dir_list.append(f)
    # print(article_list)
    # print(dir_list)         

    for dir in dir_list:
        for article in article_list:
            if dir in article:
                article_with_picture_list.append(article)
    print(article_with_picture_list)

    for article_with_picture in article_with_picture_list:
        article = Article(article_with_picture)
        article.run()


if __name__ == "__main__":
    main()