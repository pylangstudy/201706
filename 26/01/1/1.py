# coding: utf-8

import os
import gettext

_ = gettext.translation(
        domain='messages',
        localedir=os.path.join(os.path.dirname(__file__), 'locale'),
        fallback=True).gettext

def main():
    print(_('This is a translatable string.'))

if __name__ == '__main__':
    main()
