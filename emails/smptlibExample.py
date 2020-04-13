import smtplib

# gmail - smtp.gmail.com
# outlook.com/hotmail.com - smtp-mail.outlook.com
# Yahoo Mail - smtp.mail.yahoo.com

conn = smtplib.SMTP('smtp.gmail.com',587)
print(type(conn))
conn.ehlo() # Connect smtp server
conn.starttls()

conn.login('python123@gmail.com','test123') # Login method

conn.sendmail('python123@gmail.com','python123@gmail.com',
              'Subject: So long...\n\nDear Ryan,\n Thanks for all the fish.\n\n -Ryan')
conn.quit() # disconnect