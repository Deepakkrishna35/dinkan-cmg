class script(object):
    START_TXT = """𝙃𝙚𝙡𝙡𝙤 {} 😍,𝙉𝙞𝙘𝙚 𝙏𝙤 𝙈𝙚𝙚𝙩 𝙔𝙤𝙪🙌,

𝙈𝙮 𝙉𝙖𝙢𝙚 𝙄𝙨 <a href=https://t.me/{}>{}</a>, 𝙄 𝘼𝙢 𝙅𝙪𝙨𝙩 𝙖 𝙎𝙞𝙢𝙥𝙡𝙚 𝙋𝙧𝙚-𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣𝙚𝙙 𝘼𝙪𝙩𝙤𝙛𝙞𝙡𝙩𝙚𝙧 𝘽𝙤𝙩 ⚡️.
𝙄𝙩𝙨 𝙀𝙖𝙨𝙮 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 🤩. 𝙅𝙪𝙨𝙩 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝘼𝙨 𝘼𝙙𝙢𝙞𝙣, 𝙄 𝙒𝙞𝙡𝙡 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝙏𝙝𝙚𝙧𝙚 🥳"""
    HELP_TXT = """𝙃𝙚𝙮 {},
𝙃𝙚𝙧𝙚 𝙄𝙨 𝙏𝙝𝙚 𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝙈𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨..."""
    ABOUT_TXT = """✯ 𝙈𝙮 𝙉𝙖𝙢𝙚: {}⚡️
✯ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧: <a href=https://t.me/TitterBuck>☬ 𝔻𝔼𝔼ℙ𝔸𝕂 ☬</a>
✯ 𝙇𝙞𝙗𝙧𝙖𝙧𝙮: 𝙋𝙧𝙤𝙜𝙧𝙖𝙢 👨‍💻
✯ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚: 𝙋𝙮𝙩𝙝𝙤𝙣 3 
✯ 𝘿𝙖𝙩𝙖 𝘽𝙖𝙨𝙚: 𝙈𝙖𝙣𝙜𝙤 𝙙𝙗 
✯ 𝙎𝙚𝙧𝙫𝙚𝙧: 𝙃𝙚𝙧𝙤𝙠𝙪
✯ 𝘽𝙪𝙞𝙡𝙙 𝙎𝙩𝙖𝙩𝙪𝙨: 𝙫1.0.1 [ 𝘽𝙀𝙏𝘼 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝙃𝙚𝙢𝙗𝙖𝙙𝙖 𝙆𝙚𝙡𝙡𝙖𝙝𝙝... 𝙉𝙞𝙣𝙖𝙠𝙠 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 𝙏𝙝𝙖𝙧𝙪𝙡𝙡𝙖....🙂"""
    MANUELFILTER_TXT = """𝙃𝙚𝙡𝙥: <b>𝙁𝙞𝙡𝙩𝙚𝙧𝙨</b>

- 𝙁𝙞𝙡𝙩𝙚𝙧 𝙞𝙨 𝙩𝙝𝙚 𝙛𝙚𝙖𝙩𝙪𝙧𝙚 𝙬𝙚𝙧𝙚 𝙪𝙨𝙚𝙧𝙨 𝙘𝙖𝙣 𝙨𝙚𝙩 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙚𝙙 𝙧𝙚𝙥𝙡𝙞𝙚𝙨 𝙛𝙤𝙧 𝙖 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧 𝙠𝙚𝙮𝙬𝙤𝙧𝙙 𝙖𝙣𝙙 𝙀𝙫𝙖𝙈𝙖𝙧𝙞𝙖 𝙬𝙞𝙡𝙡 𝙧𝙚𝙨𝙥𝙤𝙣𝙙 𝙬𝙝𝙚𝙣𝙚𝙫𝙚𝙧 𝙖 𝙠𝙚𝙮𝙬𝙤𝙧𝙙 𝙞𝙨 𝙛𝙤𝙪𝙣𝙙 𝙩𝙝𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚

<b>𝙉𝙊𝙏𝙀:</b>
1. 𝘿𝙞𝙣𝙠𝙖𝙣 𝙨𝙝𝙤𝙪𝙡𝙙 𝙝𝙖𝙫𝙚 𝙖𝙙𝙢𝙞𝙣 𝙥𝙧𝙞𝙫𝙞𝙡𝙡𝙖𝙜𝙚.
2. 𝙤𝙣𝙡𝙮 𝙖𝙙𝙢𝙞𝙣𝙨 𝙘𝙖𝙣 𝙖𝙙𝙙 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙞𝙣 𝙖 𝙘𝙝𝙖𝙩.
3. 𝙖𝙡𝙚𝙧𝙩 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙝𝙖𝙫𝙚 𝙖 𝙡𝙞𝙢𝙞𝙩 𝙤𝙛 64 𝙘𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨.

<b>𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙐𝙨𝙖𝙜𝙚:</b>
• /filter - <code>𝙖𝙙𝙙 𝙖 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩</code>
• /filters - <code>𝙡𝙞𝙨𝙩 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙤𝙛 𝙖 𝙘𝙝𝙖𝙩</code>
• /del - <code>𝙙𝙚𝙡𝙚𝙩𝙚 𝙖 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩</code>
• /delall - <code>𝙙𝙚𝙡𝙚𝙩𝙚 𝙩𝙝𝙚 𝙬𝙝𝙤𝙡𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙞𝙣 𝙖 𝙘𝙝𝙖𝙩 (𝙘𝙝𝙖𝙩 𝙤𝙬𝙣𝙚𝙧 𝙤𝙣𝙡𝙮)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
