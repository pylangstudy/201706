# import string.Template # ModuleNotFoundError: No module named 'string.Template'; 'string' is not a package
from string import Template

markdown_template = """# $Overview 

$Details"""
#t = string.Template(markdown_template)
t = Template(markdown_template)
print( t.substitute(Overview='これは概要タイトルである', Details='これは詳細な説明文である。') )
