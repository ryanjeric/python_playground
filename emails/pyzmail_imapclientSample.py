# pip install imapclient
# pip install pyzmail
# pip install pyzmail36
import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('test1@gmail.com','password')
conn.select_folder('INBOX',readonly=True)

# imap Search KEYS
#ALL
#BEFORE date
#ON date
#SINCE date
# SUBJECT string
# BODY string
# TEXT string

UIDS = conn.search(['FROM','test2@gmail.com'])
print(UIDS)
rawmsg = conn.fetch([44],['BODY[]','FLAGS'])
print(rawmsg)

message = pyzmail.PyzMessage.factory(rawmsg[44][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))
# BODY
print(message.text_part)
print(message.html_part)
print(message.text_part.get_payload().decode('UTF-8'))
# message.text_part.charset

# DELETING
print(conn.list_folders())
conn.select_folder('INBOX',readonly=False)
conn.delete_messages([44])
conn.logout()