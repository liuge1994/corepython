from email.mine.text import MIMEText

msg = MIMEText('hello, send by Python...', '')

from_addr = raw_input('From: ')
password = raw_input('Password: ')

smtp_server = raw_input('To: ')

import smtplib

server = smtplib.SMTP(smtp_server, 25)

server.set_debuglevel(1)

server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()