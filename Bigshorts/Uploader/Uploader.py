import reels
import shorts
import tiktok


def upload(tiktok=True, youtube=True, reels=True, config={}):
    reels.upload()
    shorts.upload()
    tiktok.upload()