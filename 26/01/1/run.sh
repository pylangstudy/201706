#python3 pygettext.py 1.py
#cp messages.pot messages.po
# messages.po を手動で編集する
#python3 msgfmt.py messages.po
mkdir -p ./ja/LC_MESSAGES/
# cp messages.mo ./ja/LC_MESSAGES/messages.mo
python3 1.py
