#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import isfile, isdir, join
import subprocess

extensions = {".ASF", ".AVI", ".M1V", ".M2P", ".M2T", ".M2TS", ".M2V", ".M4V", ".MKV", ".MOV",
              ".MP4", ".MPE", ".MPG", ".MPG4", ".MTS", ".QT", ".TP", ".TRP", ".TS", ".VOB", ".WMV"}

error_message = 'Failed to get MediaInfo.'


def scan_dir(cwd):
    files = [f for f in os.listdir(cwd)]
    for f in files:
        path = join(cwd, f)
        if isdir(path):
            scan_dir(path)
        elif isfile(path):
            name, ext = os.path.splitext(f)
            if ext.upper() in extensions:
                create_index(cwd, f)


def create_index(cwd, filename):
    f = join(cwd, filename)
    cmd = u'synoindex -g "{0}" -t video'.format(f)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd,  shell=True)
    p.wait()

    if error_message in p.stdout.read():
        cmd = u'synoindex -a "{0}"'.format(join(cwd, filename))
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd,  shell=True)
        p.wait()


def to_unicode(s, encoding='utf-8'):
    if isinstance(s, basestring):
        if not isinstance(s, unicode):
            return unicode(s, encoding)
    return s


working_dir = to_unicode(os.environ.get('TR_TORRENT_DIR'))
scan_dir(working_dir)
