
import asyncio
import base64
import os
import random        
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from NIXA.data import RAID, REPLYRAID, DEADLYSPAM
from NIXA.main import BOT
from config import SUDO_USERS

OWNER_ID = SUDO_USERS
que = {}
hl = '/'


NUMBER = ["0", "1"]

LOVEOP = [
    "JAANU I LOVE U NA🥺",
    "YOU ARE MY LIFE BABY ANYONE DON'T HAVE DARE TO COME BETWEEN US 🥺😏",
   "SKY IS BLUE I GOT FLU I LOVE YOU TOO🥺",
   "I HAVE DISEASE I DON'T KNOW BUT MY FRIENDS ARE SAYING ITS YUKU'S LOVERIA 🥺",
   "WHY YOUR EYES ARE SO BEAUTIFUL 🥵",
    "I MISS U BABY I LOVE YOU BABY I TRUST U BABY🥺",
    "GOD MADE YOU ONLY FOR ME WIFEY 🥺",
    "BABY CLOSE YOUR EYES AND SEE WHAT DO YOU SEE, ITS MY LIFE WITHOUT YOU MY LOVE 🥺",
    "I DON'T KNOW WHY MY FRIENDS ARE CALLING YOU BHABHI FROM MORNING I THINK THEY FOUND ABOUT US 😉😍",
    "YOU ARE MORE SWEET THAN LIFE MY BABY🥺",
    "WHAT DO YOU MEAN YOU ARE MINE 🥵🥵🥺",
    "WILL YOU BE MY FUTURE KIDS MOM 🥺",
    "YOU MADE MY LIFE BEAUTIFUL🥺",
    "WHAT WE ARE GOING TO GET MARRY SOON😍",
    "I NEVER BELIEVED IN LOVE AT FIRST SIGHT, BUT THAT WAS BEFORE I SAW YOU ☺️☺️🙈",
    "YOU ARE MY FAVOURITE DRUUUG I GOT ADDICTION OF YOU🥺",
    "DID THE SUN COME OUT OR DID U JUST SMILE AT ME? 😍",
    "YOU ARE MY MORNING AND EVENING WIFEYYYAAA 😍😘",
    "YOU ARE MY FIRST AND LAST CHOICE🥺😍",
    "I LIKE YOUR EVERY STYLE EXCEPT BEING ANGRY 🥺😍",
    "WHEN YOU ARE ANGRY THEN SOMETHING HAPPENS TO MY HEART🥺",
    "WHY I THINK OF YOU IN MY HEART ALL TIME 🥺",
    "YOU MADE MY LIFE AND HEART HAPPY AGAIN 😍",
    "IF I DON'T SEE YOU FOR A SECOND NA ITS HURTS 🥺",
    "DO YOU HAPPEN TO HAVE A BAND-AID ? BECAUSE I SCRAPED MY KNEES FALLING FOR YOU BABY 🥺",
    "LIFE IS NOT KNOWN BUT THERE IS CONNECTION BETWEEN YOU AND MY HEART😍",
    "FOR ME YOU ARE MY EVERYTHING 😌😌",
    "WHAT WILL HAPPEN TO ME IF YOU WENT 🥺",
    "I DIDN'T KNOW WHAT I WANTED IN A WOMEN UNTILL I SAW YOU ☺️",
    "YOU ARE GOING TO GET MY SURNAME VERY SOON 😊😊😌😌",
    "I DON'T KNOW ABOUT MIND BUT MY HEART IS INSIDE YOU ☺️🙈🙈",
    "YOU ARE MY LIFE AND HEART'S DESIRE 🥺❤️",
    "YOUR EYES ARE LIKE OCEAN I CAN SWIM INTO THEM ALL DAY🥺❤️",
    "I AM YOUR KING AND YOU ARE MY QUEEN LETS MAKE A UNIQUE STORY ❤️",
    "IF THIS IS NOT LOVE THEN WHAT IS 🥺❤️",
    "I AM LOST IN YOU MY WIFEYY🥺",
    "WHY I WANT YOU SO MUCH MY LOVE ❤️🥺",
    "LOVE IS PART OF HEART AND YOU ARE MINE 🙈",
    "DON'T KNOW BRAIN THE HEART BROUGHT IT TO YOU MY WIFEY🥺",
    "WHY YOU DIRECTLY COME IN MY HEART❤️🥺",
    "I WILL UNITE HEART AND MIND TO MAKE YOU A WIFE MY BABY 🥺❤️",
    "EARLIER IN MY LIFE THERE IS LOTS OF TENSION BUT WHEN I SEE YOU MY ALL PROBLEM VANISH  🥺",
    "MY MOM IS WAITING FOR YOU AT HOME PLEASE COME ❤️🥺",
]


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sloveraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Love Raid\n\nCommand:\n\n.loveraid <count> <Username of User>\n\n.loveraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deadly:
                text = f"I can't raid on @deadly_spam_bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DEADLYSPAM:
                text = f"I can't raid on @deadly_spam_bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(LOVEOP)),
            reply_to=event.message.id,
        )


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Love ReplyRaid\n\nCommand:\n\n.lovereplyraid <Username of User>\n\n.lovereplyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in Deadly:
                text = f" can't raid on @deadly_spam_bot's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in DEADLYSPAM:
                text = f" can't raid on @deadly_spam_bot's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdlovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Deactivate Raid\n\nCommand:\n\n.dlovereplyraid <Username of User>\n\n.dlovereplyraid <reply to a User>"
    global que
    if e.sender_id in SUDO_USERS:    
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
