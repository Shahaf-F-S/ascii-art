# ascii-art

> A lightweight module for colorful ascii art generation from images and videos.

## example

```python
from ascii_art import image_ascii_art, video_ascii_art

IMAGE_SOURCE = "media/images/input/milo.png"
IMAGE_DESTINATION = "media/images/output/ascii_milo.png"

VIDEO_SOURCE = "media/videos/input/milo.mp4"
VIDEO_DESTINATION = "media/videos/output/ascii_milo.mp4"

image_ascii_art(source=IMAGE_SOURCE, destination=IMAGE_DESTINATION)
video_ascii_art(source=VIDEO_SOURCE, destination=VIDEO_DESTINATION)
```