import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC.utils.errors import capture_err
from SHUKLAMUSIC import app
from config import BOT_USERNAME

# Caption Text
start_txt = """<b>✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <u>ᴘʀᴇᴍ ᴍᴜsɪᴄ</u></b>

🚀 <b>ᴇᴀsʏ ᴅᴇᴘʟᴏʏ</b> – ᴏɴᴇ ᴄʟɪᴄᴋ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ  
🛡️ <b>ɴᴏ ʙᴀɴ ɪssᴜᴇs</b>  
🔋 <b>ʀᴜɴ 24/7 ʟᴀɢɢ-ғʀᴇᴇ</b>  
⚙️ <b>ғᴜʟʟʏ ғᴜɴᴄᴛɪᴏɴᴀʟ & ᴇʀʀᴏʀ-ғʀᴇᴇ</b>  

<i>ɴᴇᴇᴅ ʜᴇʟᴘ? sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴛᴏ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ!</i>"""

# Repo Command Handler
@app.on_message(filters.command("repo"))
async def repo_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/+8WjqAqBihwkyNzk9"),
            InlineKeyboardButton("👤 ᴏᴡɴᴇʀ", url="https://t.me/Prem_Assistant"),
        ],
        [InlineKeyboardButton("🧾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/+8WjqAqBihwkyNzk9")],
        [
            InlineKeyboardButton("🎧 ᴍᴜsɪᴄ ʙᴏᴛ", url="https://github.com/arvind021/STRANGER-MUSIC/fork"),
        ],
    ]

    await msg.reply_photo(
        photo="https://files.catbox.moe/jxribw.jpg",
        caption=start_txt,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/arvind021/STRANGER-MUSIC/contributors")

    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/arvind021/STRANGER-MUSIC) | [UPDATES](https://t.me/+8WjqAqBihwkyNzk9)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
        
