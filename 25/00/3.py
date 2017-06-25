import zipfile

s = b'witch which has which witches wrist watch'
with zipfile.ZipFile('3.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('3.txt', s)
