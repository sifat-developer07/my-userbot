from telethon import TelegramClient, events
import os


# ==========================
# TELEGRAM API
# ==========================

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

client = TelegramClient("session", api_id, api_hash)


# ==========================
# OWNER ID
# ==========================

OWNER_ID = 6985777615


# Permission users
users = [
    OWNER_ID
]


# ==========================
# PERSONAL INFO
# ==========================

BKASH = "01722329117"

NAGAD = "01629966670"


BINANCE = """
💳 BINANCE PAYMENT

👤 Name: ZX DEV

🆔 UID:
1108097450

🌐 Network:
BEP20 (BSC)

📋 WALLET ADDRESS:

0x6e78e4ad88fe9c16c253d776246a6c215ed372bd
"""


# ==========================
# HOSTING BILL DATABASE
# ==========================

hosting_bill = {

    "client1": "500 TK",

    "client2": "1000 TK",

    "client3": "1500 TK"

}



# ==========================
# COMMAND SYSTEM
# ==========================

@client.on(events.NewMessage(outgoing=True))
async def commands(event):

    text = event.raw_text.strip()

    user = event.sender_id



    # SIGNUP

    if text == "SsingUp":

        if user not in users:

            users.append(user)


        await event.edit(
            "✅ Account Activated"
        )



    # HELP

    elif text == "Shelp":

        await event.edit(
"""
🤖 USERBOT COMMANDS


🔐 SsingUp
Activate account


🧮 Sclc 1+1
Calculator


📱 Snumber
bKash + Nagad


💰 Sbnumber
Binance


🖥 Shostbill client1
Hosting bill


"""
        )



    # CALCULATOR

    elif text.startswith("Sclc "):

        if user not in users:

            await event.edit(
                "❌ No Permission"
            )

            return


        try:

            calculation = text[5:]

            answer = eval(calculation)


            await event.edit(
                f"🧮 Answer: {answer}"
            )


        except:

            await event.edit(
                "❌ Wrong Calculation"
            )



    # BKASH NAGAD

    elif text == "Snumber":


        if user not in users:

            await event.edit(
                "❌ No Permission"
            )

            return



        await event.edit(
f"""
📱 PAYMENT NUMBER


bKash:
{BKASH}


Nagad:
{NAGAD}
"""
        )



    # BINANCE

    elif text == "Sbnumber":


        if user not in users:

            await event.edit(
                "❌ No Permission"
            )

            return



        await event.edit(
            BINANCE
        )



    # HOSTING BILL

    elif text.startswith("Shostbill "):


        if user not in users:

            await event.edit(
                "❌ No Permission"
            )

            return



        client_name = text.replace(
            "Shostbill ",
            ""
        )



        if client_name in hosting_bill:


            await event.edit(
f"""
🖥 CLIENT:

{client_name}


💵 HOSTING BILL:

{hosting_bill[client_name]}
"""
            )


        else:


            await event.edit(
                "❌ Client Not Found"
            )




# START

client.start()

client.run_until_disconnected()
