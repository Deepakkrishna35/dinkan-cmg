class script(object):
    START_TXT = """𝙃𝙚𝙡𝙡𝙤 {} 😍,𝙉𝙞𝙘𝙚 𝙏𝙤 𝙈𝙚𝙚𝙩 𝙔𝙤𝙪🙌,

𝙄 𝘼𝙢 𝙅𝙪𝙨𝙩 𝙖 𝙎𝙞𝙢𝙥𝙡𝙚 𝙋𝙧𝙚-𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣𝙚𝙙 𝘼𝙪𝙩𝙤𝙛𝙞𝙡𝙩𝙚𝙧 𝘽𝙤𝙩 ⚡️
𝙄𝙩𝙨 𝙀𝙖𝙨𝙮 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 🤩. 𝙅𝙪𝙨𝙩 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝘼𝙨 𝘼𝙙𝙢𝙞𝙣, 𝙄 𝙒𝙞𝙡𝙡 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝙏𝙝𝙚𝙧𝙚 🥳"""
    HELP_TXT = """𝙃𝙚𝙮 {},
𝙃𝙚𝙧𝙚 𝙄𝙨 𝙏𝙝𝙚 𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝙈𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨..."""
    ABOUT_TXT = """➣ 𝙈𝙮 𝙉𝙖𝙢𝙚: {}⚡️
➣ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧: <a href=https://t.me/TitterBuck>☬ 𝔻𝔼𝔼ℙ𝔸𝕂 ☬</a>
➣ 𝙇𝙞𝙗𝙧𝙖𝙧𝙮: 𝙋𝙧𝙤𝙜𝙧𝙖𝙢 👨‍💻
➣ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚: 𝙋𝙮𝙩𝙝𝙤𝙣 3 
➣ 𝘿𝙖𝙩𝙖 𝘽𝙖𝙨𝙚: 𝙈𝙖𝙣𝙜𝙤𝘿𝘽
➣ 𝙎𝙚𝙧𝙫𝙚𝙧: 𝙈𝙤𝙜𝙚𝙣𝙞𝙪𝙨 
➣ 𝘽𝙪𝙞𝙡𝙙 𝙎𝙩𝙖𝙩𝙪𝙨: 𝙫1.0.1 [ 𝘽𝙀𝙏𝘼 ]"""
    SOURCE_TXT = """𝙃𝙚𝙢𝙗𝙖𝙙𝙖 𝙆𝙚𝙡𝙡𝙖𝙝𝙝... 𝙉𝙞𝙣𝙖𝙠𝙠 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 𝙏𝙝𝙖𝙧𝙪𝙡𝙡𝙖....🙂"""
    MANUELFILTER_TXT = """𝙃𝙚𝙡𝙥: <b>𝙁𝙞𝙡𝙩𝙚𝙧𝙨</b>

◉ 𝙁𝙞𝙡𝙩𝙚𝙧 𝙞𝙨 𝙩𝙝𝙚 𝙛𝙚𝙖𝙩𝙪𝙧𝙚 𝙬𝙚𝙧𝙚 𝙪𝙨𝙚𝙧𝙨 𝙘𝙖𝙣 𝙨𝙚𝙩 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙚𝙙 𝙧𝙚𝙥𝙡𝙞𝙚𝙨 𝙛𝙤𝙧 𝙖 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧 𝙠𝙚𝙮𝙬𝙤𝙧𝙙 𝙖𝙣𝙙 𝘿𝙞𝙣𝙠𝙖𝙣 𝙬𝙞𝙡𝙡 𝙧𝙚𝙨𝙥𝙤𝙣𝙙 𝙬𝙝𝙚𝙣𝙚𝙫𝙚𝙧 𝙖 𝙠𝙚𝙮𝙬𝙤𝙧𝙙 𝙞𝙨 𝙛𝙤𝙪𝙣𝙙 𝙩𝙝𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚

<b>𝙉𝙊𝙏𝙀:</b>
1. 𝘿𝙞𝙣𝙠𝙖𝙣 𝙨𝙝𝙤𝙪𝙡𝙙 𝙝𝙖𝙫𝙚 𝙖𝙙𝙢𝙞𝙣 𝙥𝙧𝙞𝙫𝙞𝙡𝙡𝙖𝙜𝙚.
2. 𝙤𝙣𝙡𝙮 𝙖𝙙𝙢𝙞𝙣𝙨 𝙘𝙖𝙣 𝙖𝙙𝙙 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙞𝙣 𝙖 𝙘𝙝𝙖𝙩.
3. 𝙖𝙡𝙚𝙧𝙩 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙝𝙖𝙫𝙚 𝙖 𝙡𝙞𝙢𝙞𝙩 𝙤𝙛 64 𝙘𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨.

<b>𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙐𝙨𝙖𝙜𝙚:</b>
◉ /filter - 𝙖𝙙𝙙 𝙖 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩
◉ /filters - 𝙡𝙞𝙨𝙩 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙤𝙛 𝙖 𝙘𝙝𝙖𝙩
◉ /del - 𝙙𝙚𝙡𝙚𝙩𝙚 𝙖 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩
◉ /delall - 𝙙𝙚𝙡𝙚𝙩𝙚 𝙩𝙝𝙚 𝙬𝙝𝙤𝙡𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙞𝙣 𝙖 𝙘𝙝𝙖𝙩 (𝙘𝙝𝙖𝙩 𝙤𝙬𝙣𝙚𝙧 𝙤𝙣𝙡𝙮)"""
    BUTTON_TXT = """𝙃𝙚𝙡𝙥: <b>𝘽𝙪𝙩𝙩𝙤𝙣𝙨</b>

◉ 𝘿𝙞𝙣𝙠𝙖𝙣 𝙎𝙪𝙥𝙥𝙤𝙧𝙩𝙨 𝙗𝙤𝙩𝙝 𝙪𝙧𝙡 𝙖𝙣𝙙 𝙖𝙡𝙚𝙧𝙩 𝙞𝙣𝙡𝙞𝙣𝙚 𝙗𝙪𝙩𝙩𝙤𝙣𝙨.

<b>𝙉𝙊𝙏𝙀:</b>
1. 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙬𝙞𝙡𝙡 𝙣𝙤𝙩 𝙖𝙡𝙡𝙤𝙬𝙨 𝙮𝙤𝙪 𝙩𝙤 𝙨𝙚𝙣𝙙 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙬𝙞𝙩𝙝𝙤𝙪𝙩 𝙖𝙣𝙮 𝙘𝙤𝙣𝙩𝙚𝙣𝙩, 𝙨𝙤 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙞𝙨 𝙢𝙖𝙣𝙙𝙖𝙩𝙤𝙧𝙮.
2. 𝘿𝙞𝙣𝙠𝙖𝙣 𝙨𝙪𝙥𝙥𝙤𝙧𝙩𝙨 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙬𝙞𝙩𝙝 𝙖𝙣𝙮 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙢𝙚𝙙𝙞𝙖 𝙩𝙮𝙥𝙚.
3. 𝘽𝙪𝙩𝙩𝙤𝙣𝙨 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙥𝙧𝙤𝙥𝙚𝙧𝙡𝙮 𝙥𝙖𝙧𝙨𝙚𝙙 𝙖𝙨 𝙢𝙖𝙧𝙠𝙙𝙤𝙬𝙣 𝙛𝙤𝙧𝙢𝙖𝙩

<b>𝙐𝙍𝙇 𝙗𝙪𝙩𝙩𝙤𝙣𝙨:</b>
<code>[Button Text](buttonurl:https://t.me/DinkanBot)</code>

<b>𝘼𝙡𝙚𝙧𝙩 𝙗𝙪𝙩𝙩𝙤𝙣𝙨:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝙃𝙚𝙡𝙥: <b>𝘼𝙪𝙩𝙤 𝙁𝙞𝙡𝙩𝙚𝙧</b>

<b>𝙉𝙊𝙏𝙀:</b>
1. 𝙈𝙖𝙠𝙚 𝙢𝙚 𝙩𝙝𝙚 𝙖𝙙𝙢𝙞𝙣 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙞𝙛 𝙞𝙩'𝙨 𝙥𝙧𝙞𝙫𝙖𝙩𝙚.
2. 𝙢𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙙𝙤𝙚𝙨 𝙣𝙤𝙩 𝙘𝙤𝙣𝙩𝙖𝙞𝙣𝙨 𝙘𝙖𝙢𝙧𝙞𝙥𝙨, 𝙥𝙤𝙧𝙣 𝙖𝙣𝙙 𝙛𝙖𝙠𝙚 𝙛𝙞𝙡𝙚𝙨.
3. 𝙁𝙤𝙧𝙬𝙖𝙧𝙙 𝙩𝙝𝙚 𝙡𝙖𝙨𝙩 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙩𝙤 𝙢𝙚 𝙬𝙞𝙩𝙝 𝙦𝙪𝙤𝙩𝙚𝙨.
 𝙄'𝙡𝙡 𝙖𝙙𝙙 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙛𝙞𝙡𝙚𝙨 𝙞𝙣 𝙩𝙝𝙖𝙩 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙩𝙤 𝙢𝙮 𝙙𝙗."""
    CONNECTION_TXT = """𝙃𝙚𝙡𝙥: <b>𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙤𝙣𝙨</b>

◉ 𝙐𝙨𝙚𝙙 𝙩𝙤 𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙗𝙤𝙩 𝙩𝙤 𝙋𝙈 𝙛𝙤𝙧 𝙢𝙖𝙣𝙖𝙜𝙞𝙣𝙜 𝙛𝙞𝙡𝙩𝙚𝙧𝙨.
◉ 𝙞𝙩 𝙝𝙚𝙡𝙥𝙨 𝙩𝙤 𝙖𝙫𝙤𝙞𝙙 𝙨𝙥𝙖𝙢𝙢𝙞𝙣𝙜 𝙞𝙣 𝙜𝙧𝙤𝙪𝙥𝙨.

<b>𝙉𝙊𝙏𝙀:</b>
1. 𝙊𝙣𝙡𝙮 𝙖𝙙𝙢𝙞𝙣𝙨 𝙘𝙖𝙣 𝙖𝙙𝙙 𝙖 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙤𝙣.
2. 𝙎𝙚𝙣𝙙 <code>/connect</code> 𝙛𝙤𝙧 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙣𝙜 𝙢𝙚 𝙩𝙤 𝙪𝙧 𝙋𝙈.

<b>𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙐𝙨𝙖𝙜𝙚:</b>
◉ /connect  - 𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙖 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧 𝙘𝙝𝙖𝙩 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙋𝙈
◉ /disconnect  - 𝙙𝙞𝙨𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙛𝙧𝙤𝙢 𝙖 𝙘𝙝𝙖𝙩
◉ /connections - 𝙡𝙞𝙨𝙩 𝙖𝙡𝙡 𝙮𝙤𝙪𝙧 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙤𝙣𝙨"""
    EXTRAMOD_TXT = """𝙃𝙚𝙡𝙥: <b>𝙀𝙭𝙩𝙧𝙖 𝙈𝙤𝙙𝙪𝙡𝙚𝙨</b>

<b>𝙉𝙊𝙏𝙀:</b>
𝙩𝙝𝙚𝙨𝙚 𝙖𝙧𝙚 𝙩𝙝𝙚 𝙚𝙭𝙩𝙧𝙖 𝙛𝙚𝙖𝙩𝙪𝙧𝙚𝙨 𝙤𝙛 𝘿𝙞𝙣𝙠𝙖𝙣

<b>𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙐𝙨𝙖𝙜𝙚:</b>
◉ /id - 𝙜𝙚𝙩 𝙞𝙙 𝙤𝙛 𝙖 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙚𝙙 𝙪𝙨𝙚𝙧.
◉ /info  - 𝙜𝙚𝙩 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙖𝙗𝙤𝙪𝙩 𝙖 𝙪𝙨𝙚𝙧.
◉ /imdb  - 𝙜𝙚𝙩 𝙩𝙝𝙚 𝙛𝙞𝙡𝙢 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙛𝙧𝙤𝙢 𝙄𝙈𝘿𝙗 𝙨𝙤𝙪𝙧𝙘𝙚.
◉ /search  - 𝙜𝙚𝙩 𝙩𝙝𝙚 𝙛𝙞𝙡𝙢 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙛𝙧𝙤𝙢 𝙫𝙖𝙧𝙞𝙤𝙪𝙨 𝙨𝙤𝙪𝙧𝙘𝙚𝙨."""
    ADMIN_TXT = """𝙃𝙚𝙡𝙥: <b>𝘼𝙙𝙢𝙞𝙣 𝙢𝙤𝙙𝙨</b>

<b>𝙉𝙊𝙏𝙀:</b>
𝙏𝙝𝙞𝙨 𝙢𝙤𝙙𝙪𝙡𝙚 𝙤𝙣𝙡𝙮 𝙬𝙤𝙧𝙠𝙨 𝙛𝙤𝙧 𝙢𝙮 𝙖𝙙𝙢𝙞𝙣𝙨

<b>𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙐𝙨𝙖𝙜𝙚:</b>
◉ /logs - 𝙩𝙤 𝙜𝙚𝙩 𝙩𝙝𝙚 𝙧𝙚𝙨𝙘𝙚𝙣𝙩 𝙚𝙧𝙧𝙤𝙧𝙨
◉ /stats - 𝙩𝙤 𝙜𝙚𝙩 𝙨𝙩𝙖𝙩𝙪𝙨 𝙤𝙛 𝙛𝙞𝙡𝙚𝙨 𝙞𝙣 𝙙𝙗
◉ /delete - 𝙩𝙤 𝙙𝙚𝙡𝙚𝙩𝙚 𝙖 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘 𝙛𝙞𝙡𝙚 𝙛𝙧𝙤𝙢 𝙙𝙗
◉ /users - 𝙩𝙤 𝙜𝙚𝙩 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙢𝙮 𝙪𝙨𝙚𝙧𝙨 𝙖𝙣𝙙 𝙞𝙙𝙨
◉ /chats - 𝙩𝙤 𝙜𝙚𝙩 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙩𝙝𝙚 𝙢𝙮 𝙘𝙝𝙖𝙩𝙨 𝙖𝙣𝙙 𝙞𝙙𝙨
◉ /leave  - 𝙩𝙤 𝙡𝙚𝙖𝙫𝙚 𝙛𝙧𝙤𝙢 𝙖 𝙘𝙝𝙖𝙩
◉ /disable  -  𝙙𝙤 𝙙𝙞𝙨𝙖𝙗𝙡𝙚 𝙖 𝙘𝙝𝙖𝙩
◉ /ban  - 𝙩𝙤 𝙗𝙖𝙣 𝙖 𝙪𝙨𝙚𝙧
◉ /unban  - 𝙩𝙤 𝙪𝙣𝙗𝙖𝙣 𝙖 𝙪𝙨𝙚𝙧
◉ /channel - 𝙩𝙤 𝙜𝙚𝙩 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙩𝙤𝙩𝙖𝙡 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙 𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨
◉ /broadcast - 𝙩𝙤 𝙗𝙧𝙤𝙖𝙙𝙘𝙖𝙨𝙩 𝙖 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙩𝙤 𝙖𝙡𝙡 𝙪𝙨𝙚𝙧𝙨"""
    STATUS_TXT = """➣ 𝙏𝙤𝙩𝙖𝙡 𝙁𝙞𝙡𝙚𝙨: <code>{}</code>
➣ 𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨: <code>{}</code>
➣ 𝙏𝙤𝙩𝙖𝙡 𝘾𝙝𝙖𝙩𝙨: <code>{}</code>
➣ 𝙏𝙤𝙩𝙖𝙡 𝙎𝙩𝙤𝙧𝙖𝙜𝙚𝙨: <code>{}</code> 𝙼𝚒𝙱
➣ 𝙁𝙧𝙚𝙚 𝙎𝙩𝙤𝙧𝙖𝙜𝙚𝙨: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#𝙉𝙚𝙬𝙐𝙨𝙚𝙧
𝙄𝘿 - <code>{}</code>
𝙉𝙖𝙢𝙚 - {}
"""
