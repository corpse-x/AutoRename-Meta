import re, os, time
id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29478593")
    API_HASH  = os.environ.get("API_HASH", "24c3a9ded4ac74bab73cbe6dafbc8b3e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6515426684:AAFM81JO1DYXyyD5Fvlo1Ds2-X5y3Cxz3lk")

    # database config
    DB_NAME = os.environ.get("DB_NAME","autorename")
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://arnavgupta0078:arnav@cluster3301.ojyvd.mongodb.net/test?retryWrites=true&w=majority")

    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN="1997042805, 2008011703, 6331067820, 5053815620, 6886483871, 5400174180, 6693143450, 6259443940"
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- #
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'paradoxdumps,yukiLOGS').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002092954715"))
    PORT = int(os.environ.get("PORT", "8000"))

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", "False"))

    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFYDxgAIPAvs7Th3NFDT6cxUpw1qUj7TfHY9oUXDOOyP4XIz-Yk7V5maZhq9w5jrP1-ClRxWCy4q3gO5usNnU745eV2Npr8veKWywaM_3zkTDhtSS8JaSni1chkhcF7PltYoM5IbMFAlPFazOWU5pkxkCxayp9AITtb1G7CjJJ3X6MyYjVtyC2NAI7kNdpekqXZ10IWv6eH6k8ULadzx2AVR8LiNovDhhaBgteHqDODeINYVT26_YnF8EHN6dIktKg7L0x7OG0ypWmpgWGqcgfn4Z2Cpbjd92G8E61PhaDZAHdbl14i2PCij4kliwXPYSMdLatFNn8gK6_-gdgp1UQ0Ou4e_AAAAAGbx_v_AA")
class Txt(object):
    # part of text configuration

    START_TXT = """Nigga {} chup

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Auto Rename Of Your Files.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

➻ Use /tutorial Command To Know How To Use Me.

<b> ;) </b>

<b> Under : @STERN_LEGION </b>
"""

    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @AnimePlaza_STR</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """

    ABOUT_TXT = f"""<b> Myself :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0.106</a>
<b>🚀 Server :</b> <a href='https://google.com'>Linux Local</a>
<b>[×] Developer :</b> <a href='https://t.me/ghost_kun'>ghost</a>
"""


    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>

⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....

⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>

⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼  CHUP AND GM
╰━━━━━━━━━━━━━━━➣ </b>"""


    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>My UPI - contact @ghost_kun </b> """

    HELP_TXT = """<b>Hey Nigga</b> {}

Give up and Die, might help u """