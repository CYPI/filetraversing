import argparse
import os
import re
import fileinput


def analyticsupdate(arg, dirname, files):
  for file in files:
  fullfilepath = os.path.join(dirname, file)
  for line in fileinput.input(fullfilepath, inplace=True):
    if re.search(r'UA-\d{8}-\d', line):
      print re.sub(r'UA-\d{8}-\d', arg, line)
    else:
      print line.strip()

def main():

  app_caption = 'replace Google Analytics userid in all the file in a directory'
  app_caption_userid = 'new Google Analytics userid to apply'
  app_caption_root = 'root directory to start updating your Google Analytics userid'

  parser = argparse.ArgumentParser(description=app_caption)
  parser.add_argument('-u', type=str, help=app_caption_userid)
  parser.add_argument('-r', type=str, help=app_caption_root)

  argument = parser.parse_args()

  if argument.u and argument.r:
    os.path.walk(argument.r, analyticsupdate, argument.u)
  else:
    print 'provid a new userid and a root directory'

if __name__ == '__main__':
main()
