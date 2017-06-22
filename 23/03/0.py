import re
print(re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', '私は2000-01-01に生まれて2099-12-31に死にました。'))
print(re.sub(r'd..', r'AAA', 'abc def ghi abcdcba'))
print('吾輩は猫である。'.replace('猫', '神'))
