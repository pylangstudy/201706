class Main:
    def run(self, reader):
        print(type(reader))
        for record in reader.read():
            print(record)
class TsvFileReader:
    def __init__(self, file_object):
        self.__f = file_object
    def read(self):
        result = []
        for line in self.__f: result.append(line[:-1].split('\t'))
        return result
class StringReader:
    def __init__(self, string): self.__s = string
    def read(self):
        result = []
        for line in self.__s.split('\n'): result.append(line.split('\t'))
        return result

m = Main()
s = StringReader("""name	age
Yamada	50
Tanaka	40
Wada	30""")
f = open('1.tsv')
t = TsvFileReader(f)

m.run(s)
m.run(t)
f.close()
