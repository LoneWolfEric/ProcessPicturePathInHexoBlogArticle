import re
art = 'test'
line = '![IMG20180419200616](/home/luyuxuan/ProcessPicturePathInHexoBlogArticle/test/IMG20180419200616.jpg)'
get = re.findall(r'!\[.{0,100}\]\(.{0,10000}\)', line)
get = get[0]
new_path = get[0 : get.index('(') + 1] + get[get.index(art) : ]
print(new_path)