# (c) @trtechguide

import os


class Config(object):
	API_ID = int(os.environ.get("APITELEGRAM_ID"))
	API_HASH = os.environ.get("APITELEGRAM_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	GOFILE_API = os.environ.get("GOFILE_API")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_KEY")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
	SESSION_NAME = os.environ.get("SESSION_NAME", "CloudUploadManagerBot")
	BOT_OWNER = int(os.environ.get("BOTOWNER_ID"))
	LOG_CHANNEL = int(os.environ.get("CHANNEL_ID"))
	DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
	HELP_TEXT = """
Send me any Media & Choose Upload Server,
I will Upload the Media to that server.

Currently I can Upload to:
> GoFile.io
> Streamtape.com
> Pixeldrain.com

Also I can do a lot of things from Inline!
__Check Below Buttons >>>__
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
