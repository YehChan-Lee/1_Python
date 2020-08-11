import re

test_num = "저의 전화번호는 010-6666-7777"
test_str = '''i am Park Jeong-tae.I live in Paju.
I lived in Paju for 25 years.
Sample text fro testing:
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@?#$%^&*();|/<>
12345 -98.7.3.141 .6180 9,000 +42'''

pattern = re.compile('[a-zA-Z0-9]')
pattern1 = re.compile('[a-zA-Z]+')
pattern2 = re.compile('\d{3}-\d{4}-\d{4}')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
e = pattern2.findall(test_num)

print(c)
print(d)
print(e)

pattern3 = re.compile('\w+')
f = pattern3.findall(test_str)
print(f)

pattern4 = re.compile('t?est\w*')
g = pattern4.findall(test_str)
print(g)