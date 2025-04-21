# -*- encoding = utf-8 -*-
# author : houliabc

print(ord('a'))  # ordinary
print(chr(99))  # character

print('\u4e2d\u6587')  # 中文，字符的unicode编码

x = b'ABC'
print(x)  # b'ABC'，字节串
print(x.decode('utf-8'))  # ABC，字节串解码为字符串
print(x.decode('ascii'))

print((x.decode('utf-8')+'gg\xe4b8').encode('ascii',errors='ignore'))  # 用errors='ignore'忽略bytes中无法解码的字符

print(len(b'\xe4\xb8\xad\xe6\x96\x87'))