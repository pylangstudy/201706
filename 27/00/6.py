import locale
#locale.setlocale(locale.LC_ALL, 'English_United States.1252') # locale.Error: unsupported locale setting
print(locale.setlocale(locale.LC_ALL, ''))
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True)) # '1,234,567'
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
print(locale.currency(1000000, grouping=True))
