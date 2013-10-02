Synology Media Index Hook for Transmission
----

Media files downloaded via Transmission are not indexed on Synology NAS. Therefore, downloaded files are not visible to Video Statition. This simple hook allows you to index downloaded media files. Now, you can enjoy your newly downloaded video on your TV via DLNA without hassle.

(Why don't you try [Remote Transmission ++](https://chrome.google.com/webstore/detail/remote-transmission-%2B%2B/kfbocdnicmioodheiciijiegbmfoliim) chrome extension to download directly from your web browser to remote Synology NAS? And it gives you a way to choose destination folder among pre-registered folders.)

### Installation

1. Install Python via Package Center

1. Login to root via SSH
	1. Enabling SSH on Synology NAS: Control Panel > (Network Service) Terminal > Enable SSH service
    1. > ssh -lroot *yourdomain.com*
    
1. Change terminal encoding to UTF-8 unless you will not download files with non-ASCII name.
    1. Add below to /etc/profile
        > export LC_ALL=en_US.UTF-8
        >
        > export LANG=en_US.UTF-8
        >
        > export LANGUAGE=en_US.UTF-8

1. Locate **build-media-index.py** script file to **/usr/local/transmission/bin/** and give it right permission like:
    > chmod +x build-media-index.py
    >
    > chown transmission build-media-index.py
    >
    > chgrp root build-media-index.py

1. Register download completion hook for transmission.
	1. Stop transmission service temporarily.
	1. Edit **/usr/local/transmission/var/settings.json** like:
        > "script-torrent-done-enabled": true,
        >
        > "script-torrent-done-filename": "/usr/local/transmission/bin/build-media-index.py",
    1. Resume transmission service
    
1. Enjoy!
