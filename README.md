# tiktok-video-dl-py

A small Python script to download videos from TikTok from the command line.

# Disclaimer

Do not download videos which you do not have permission.

## Installation

Use git

```bash
git clone https://github.com/ZXZhIGVsZmll/tiktok-video-dl-py.git --depth=1
cd tiktok-video-dl-py
pip install -r requirements.txt
```

If you don't want to type python everytime you run the script

```bash
chmod u+x tiktok-vdl-cli.py
```

## Usage/Examples

Downloading Big Buck Bunny video

```bash
cd tiktok-video-dl-py
python tiktok-vdl-cli.py https://www.tiktok.com/@arujiisochiasu/video/6895595198034873601
```

or 

``` bash
cd tiktok-video-dl-py
./tiktok-vdl-cli.py https://www.tiktok.com/@arujiisochiasu/video/6895595198034873601
```

Note: Remove ampersand(s) "&" from link if you don't want Bash to run it in the background.

To show Help/Usage use the `--help` flag.

## Features
- Provide a path/filename using --ouput parameter
- Show info using --info parameter

## Roadmap
:black_square_button: Add GUI


## License

[The Unlicense](https://unlicense.org)
