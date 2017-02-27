import os
import argparse


def tree(root):
    for dirpath, dirs, files in os.walk(root):
        path = dirpath.split('/')
        print '|', len(path)*'---', '['+os.path.basename(dirpath)+']'
        for f in files:
            print '|', len(path)*'---', f


def main():

    app_caption = 'display a directory file tree'
    app_caption_root = 'directory root path'

    parser = argparse.ArgumentParser(description=app_caption)
    parser.add_argument('-r', type=str, help=app_caption_root)

    args = parser.parse_args()

    if args.r:
        return tree(args.r)
    else:
        print 'need a root'

if __name__ == '__main__':
    main()