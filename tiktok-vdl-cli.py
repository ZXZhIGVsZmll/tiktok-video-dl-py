#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple Tiktok video downloader using BeautifulSoup and requests"""
import argparse
import json
import re

import bs4
import requests

def main():
    """The main function"""
    ## argparse
    parser = argparse.ArgumentParser(description='Download video from Tiktok')
    parser.add_argument('url', type=str, help='Provide a Tiktok post URL')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', '--output', type=str, help='Specify location or filename of downloaded file')
    group.add_argument('-i', '--info', choices=['all', 'video', 'music', 'stats', 'author-stats'], help='Show info about the video')
    # group.add_argument('-i', '--info', action='store_true', help='Show info about the video')
    args = parser.parse_args()

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url = args.url
    filename = args.output
    info_level = args.info

    print('Fetching data . . .')

    # Prepairing the soup
    req = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    document = soup.select('#SIGI_STATE')[0].get_text()

    patt_input = r'\/video\/(\d+)'
    vid_id = re.search(patt_input, url).group(1)
    dl_url = json.loads(document)['ItemModule'][vid_id]['video']['downloadAddr']
    r_vid_id = requests.get(dl_url)
    
    if info_level:
        if info_level == 'all':
            parsed_info = json.loads(document)['ItemModule'][vid_id]
        elif info_level == 'video':
            parsed_info = json.loads(document)['ItemModule'][vid_id]['video']
        elif info_level == 'music':
            parsed_info = json.loads(document)['ItemModule'][vid_id]['music']
        elif info_level == 'stats':
            parsed_info = json.loads(document)['ItemModule'][vid_id]['stats']
        elif info_level == 'author-stats':
            parsed_info = json.loads(document)['ItemModule'][vid_id]['authorStats']

        print(json.dumps(parsed_info, indent=4))
    else:
        # Writing to output to file
        if filename == None:
            with open(vid_id + '.mp4', 'wb') as video_file:
                video_file.write(r_vid_id.content)
                print(f'Saved as {vid_id}.mp4')
        else:
            patt = r'\.mp4'
            if re.search(patt, filename) == None:
                filename = filename + '.mp4'
            with open(filename, 'wb') as video_file:
                video_file.write(r_vid_id.content)
                print(f'Saved as {filename}')

if __name__ == '__main__':
    main()
