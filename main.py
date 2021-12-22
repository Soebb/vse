from videocr import save_subtitles_to_file
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os


BOT_TOKEN = " "
API_ID = " "
API_HASH = " "

Bot = Client(
    "Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

@Bot.on_message(filters.private & filters.video)
async def main(bot, m):
    await m.reply("`Downloading and Extracting...`", parse_mode='md')
    await m.download("temp/vid.mp4")
    #if __name__ == '__main__':  # This check is mandatory for Windows.
    save_subtitles_to_file('temp/vid.mp4', 'temp/subtitle.srt', lang='fa', time_start='0:00', time_end='', conf_threshold=75, sim_threshold=80, use_fullframe=False, det_model_dir=None, rec_model_dir=None, use_gpu=False, brightness_threshold=None, similar_image_threshold=100, similar_pixel_threshold=25, frames_to_skip=1, crop_x=None, crop_y=None, crop_width=None, crop_height=None)
    await m.reply_document(document="temp/subtitle.srt")


Bot.run()
