import amino
import asyncio
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.SPRING_GREEN_3A + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminospamfxck", font="gothic"))

async def main():
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	msg = input("Message >> ")
	msgtype = input("Message Type >> ")
	clients = await client.sub_clients(start=0, size=100)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	chats = await sub_client.get_chat_threads(size=100)
	for z, title in enumerate(chats.title, 1):
		print(f"{z}.{title}")
	chatx = chats.chatId[int(input("Select The Chat >> "))-1]
	while True:
		print("Spamming...")
		await asyncio.gather(*[asyncio.create_task(sub_client.send_message(chatx, msg, msgtype)) for _ in range(100)])
		
asyncio.get_event_loop().run_until_complete(main())
