import gettext

#ja = gettext.translation('messages', localedir='/tmp/0/ja/LC_MESSAGES', languages=['ja'])
#print(ja('This is a translatable string.'))

gettext.bindtextdomain('messages')
gettext.textdomain('messages')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))


