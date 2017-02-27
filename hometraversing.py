import os
import argparse


def directories(root):
    for dirpath, dirs, files in os.walk(root):
        print(dirpath)

def main():

    app_caption = 'display dirs in your root'
    app_caption_root = 'root directory'

    parser = argparse.ArgumentParser(description=app_caption)
    parser.add_argument('-r', type=str, help=app_caption_root)

    args = parser.parse_args()

    if args.r:
        root = args.r
        return directories(root)
    else:
        return 'provide a root dir'

if __name__ == '__main__':
    main()