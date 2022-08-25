import amino
from threading import Thread
from pyfiglet import figlet_format
from colored import fore, style, attr
attr(0)
print(f"""{fore.SPRING_GREEN_3A + style.BOLD}
Script by zeviel
Github : https://github.com/zeviel""")
print(figlet_format("13MINXZP2MFXKK", font="gothic"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
chats = sub_client.get_chat_threads(size=100)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]
message = input("-- Message::: ")
message_type = int(input("-- Message Type::: "))
while True:
	print("Spamming...")
	_ = [Thread(target=sub_client.send_message, args=(chat_id, message, message_type)).start() for _ in range(5000)]
