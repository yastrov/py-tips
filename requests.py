#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# See:
# http://docs.python-requests.org/en/latest/user/advanced/

"""
Download files with requests module. Session (Keep-Alive) support.
Y.A.
"""

import requests
import re
import os
import time
from urllib.parse import urlparse

dest_folder = os.getcwd()
timeout = 5
regexp = re.compile(r'"(http://.+?)"')

def download_file(url, file_path=None, session=None):
    """
    url - url;
    file_path - path for save download files;
    session - requests.Session() object;

    return
    file_size - content-length;
    fname - filename of saved file.

    Download and safe file with requests.
    Also, you may use partial:
    from functools import partial
    for functional style.
    """
    file_path = file_path or os.getcwd()
    local_fname, r = None, None
    try:
        up = urlparse(url)
        local_fname = os.path.basename(up.path)
    except:
        local_fname = url.split('/')[-1]
    fname = os.path.join(file_path, local_fname)
    session = session or requests
    r = session.get(url, stream=True)
    file_size = r.headers['content-length']
    with open(fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        f.flush()
        os.fsync(f.fileno())
    return file_size, fname

agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0'
agent_dct = {'User-Agent': agent}
# Take list of urls from web page
r = requests.get('http://', headers=agent_dct)
html_data = r.text
raw_url_list = regexp.findall(html_data)

with requests.Session() as s:
    s.headers.update(agent_dct)
    # Nearest code may be solution like
    # functional style: map, filter
    for url in raw_url_list:
        if url.startswith('https://mega.co.nz/'):
            continue
        if not url.endswith('.mp3'):
            continue
        up = urlparse(url)
        fname = os.path.basename(up.path)
        try:
            path = os.path.join(dest_folder, fname)
        except:
            print('Invalid fname: {}'.format(fname))
            continue
        if os.path.exists(path):
            print("Exist: {}".format(path))
            continue # I know about it.
            st = os.stat(path)
            r = s.head(url=url)
            if r.status_code == 200:
                file_size = r.headers['content-length']
                if st.st_size == file_size:
                    continue
        # Get file
        print("-------------------------")
        print("Downloading: {}".format(url))
        file_size, fname = download_file(url, session=s)
        print("Downloaded: {}\nBytes: {}".format(path, file_size))
        print("-------------------------")
        time.sleep(timeout)
