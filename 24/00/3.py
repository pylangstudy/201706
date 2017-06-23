# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

""" smtp.mail.yahoo.co.jp に送信する """

addr_from = '何らかのアドレス@yahoo.co.jp'
addr_to = '何らかのアドレス@yahoo.co.jp'
password = '何らかのパスワード'
title = 'タイトル'
body = """To: {1}
From: {0}

メールの本文。
複数行で日本語も送れる。
""".format(addr_from, addr_to)
encoding = 'iso-2022-jp'

message = MIMEText(
    body.encode(encoding),
    "plain",
    encoding,
    )
message['Subject'] = str(Header(title, encoding))
#message['From'] = "%s <%s>" % (str(Header('From', encoding)), addr_from)
message['From'] = "%s <%s>" % (str(Header('送り主の別名', encoding)), addr_from)
message['To'] = "%s <%s>" % (str(Header('To', encoding)), addr_to)
message['Date'] = formatdate()
print(message)

servers = {'yahoo.co.jp': {'address': 'smtp.mail.yahoo.co.jp', 'port': 587}}

s = smtplib.SMTP(servers['yahoo.co.jp']['address'], servers['yahoo.co.jp']['port'])
s.ehlo()
#s.starttls() # smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.
s.login(addr_from, password)
#s.sendmail(addr_from, [addr_to], body)
s.sendmail(addr_from, [addr_to], message.as_string())
s.quit()

# ポート番号: 25, 465, 587
# https://docs.python.jp/3/library/smtplib.html#module-smtplib
# https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13102106493
# https://teratail.com/questions/48316

# message['From'] = ... で指定してある"%s <%s>"の書式通りにならない（yahooメールをブラウザで確認したときの挙動）
# * str(Header('...')) の内容がASCII文字だけだと <%s> 部分が表示されない
# * str(Header('...')) の内容に日本語が含まれると <%s> も表示された上、その後ろに@yahoo.co.jpが勝手に付与される

