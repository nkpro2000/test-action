import re

with open('content','r') as content:
  contents = content.read().splitlines()

with open('README.md','r') as readme:
  pre = readme.read()

with open('README.md','w') as readme:
  readme.write(re.sub('```content[\s\S]*```','```content\n'+'\n'.join(contents)+'\n```',pre))
