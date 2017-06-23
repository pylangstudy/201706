import smtplib

addr_from = '何らかのアドレス@yahoo.co.jp'
addr_to = '何らかのアドレス@yahoo.co.jp'
password = '何らかのパスワード'
body = """To: {1}
From: {0}
...
Beware the Ides of March.
""".format(addr_from, addr_to)
servers = {'yahoo.co.jp': {'address': 'smtp.mail.yahoo.co.jp', 'port': 587}}

s = smtplib.SMTP(servers['yahoo.co.jp']['address'], servers['yahoo.co.jp']['port'])
s.ehlo()
#s.starttls() # smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.
s.login(addr_from, password)
s.sendmail(addr_from, addr_to, body)
s.quit()


# ポート番号: 25, 465, 587
# https://docs.python.jp/3/library/smtplib.html#module-smtplib
# https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13102106493
# https://teratail.com/questions/48316

# タイトルも本文もないメールアドレスが送信された。
