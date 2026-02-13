# Install `yt-dlp` from Git (manual method)

## 1) Clone the repo and build the standalone binary

```bash
git clone https://github.com/yt-dlp/yt-dlp.git
cd yt-dlp
```

## 2) Make it executable globally

```bash
sudo cp dist/yt-dlp /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

## 3) Verify

```bash
yt-dlp --version
```

**Notes**

- You can update later by pulling the repo and rebuilding: `git pull` then rerun the build script and copy the new binary.
- `/usr/local/bin` is typically in `PATH` on macOS/Linux; adjust if your system differs.

## 4) Downlaod a video from youtube using yt-dlp
```bash
yt-dlp https://www.youtube.com/watch?v=VIDEO_ID
```