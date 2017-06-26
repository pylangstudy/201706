import textwrap
doc = """textwrapは指定字数に改行コードを挿入した文字列を返すらしい。ただし丁度その字数目ではない。単語単位で区切る。単語は半角スペース区切りで識別される英語仕様。日本語ではどうなるか。"""
print(textwrap.fill(doc, width=40))
