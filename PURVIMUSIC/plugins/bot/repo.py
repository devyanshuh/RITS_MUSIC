from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PURVIMUSIC import app
from config import BOT_USERNAME
from PURVIMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓᴄσмє fσʀ ᴀℓᴘʜᴀ ʀєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/@Rits_x_Music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/thala_elclassico_07"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ll_WAR_MN8_ll"),
          ],
               [
                InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟 𝗕𝗢𝗧", url=f"https://github.com/TEAMPURVI/ALPHA_BANALL"),

],
[
              InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/Adithakur008/DESTROYER_USERBOT"),
              InlineKeyboardButton("︎𝗥𝗜𝗧𝗦𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/devyanshuh/RITS_MUSIC"),
              ],
              [
              InlineKeyboardButton("𝗝𝗨𝗡𝗜𝗢𝗥 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TEAMPURVI/ALPHA_MUSIC"),
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗕𝗢𝗧 ", url=f"https://github.com/TEAMPURVI/PURVI_STRING"),
],
[
InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://github.com/Adithakur008/DESTROYER_SPAM"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TEAMPURVI/PURVI_CHAT"),
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/1aab3e5edf0611a7ef4cb.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="."))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/TEAMPURVI/PURVI_MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/devyanshuh/RITS_MUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/thala_elclassico_07)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


