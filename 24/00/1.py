import smtplib
server = smtplib.SMTP('localhost')
addr_from = 'ytyaru@yahoo.co.jp'
addr_to = 'ytyaru@live.jp'
server.sendmail(addr_from, addr_to,
"""To: {1}
From: {0}
...
Beware the Ides of March.
日本語も送れるかな？
""".format(addr_from, addr_to))
server.quit()
