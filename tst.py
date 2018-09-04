import re

get = re.search(r'!\[.{0,100}\]\(.{0,10000}\)', '![IMG20180419200616](/home/luyuxuan/ProcessPicturePathInHexoBlogArticle/test/IMG20180419200616.jpg)')

print(get)