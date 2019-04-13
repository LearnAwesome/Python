''' 8bit = 1byte，所以1byte最大数字是11111111(二进制)，255(十进制) '''

# 字符的三种编码
'''
* ASCII编码。只支持英文等简单的128个编码，只占1byte
* Unicode编码。支持全语言，但至少占有2byte
* UTF-8编码。支持全语言，对于原始ASCII编码占位相同
'''

# 计算机系统通用的字符编码工作方式
''' 在计算机内存中统一使用Unicode编码，当需要储存到硬盘或者传输的时候，就转换为UTF-8编码 '''

# global@ord() 将字符串转换为Unicode编码
print( ord('A') ); # 65
print( ord('中') ); # 20013
# global@chr() 将Unicode编码转换为字符串
print( chr(65) ); # 'A'
print( chr(20013) ); # '中'

# str@encode() 字符串str => 字节流bytes
print( 'ABC'.encode('ascii') ); # b'ABC'
print( '中文'.encode('utf-8') ); # b'\xe4\xb8\xad\xe6\x96\x87'
# str@decode() 字节流bytes => 字符串str
print( b'ABC'.decode('ascii') ); # 'ABC'
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') ); # '中文'
print( b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') ) # '中' 对于无法转换的报错处理

# global@len() 计算长度
print( len('ABC') ); # 3
print( len('中文') ); # 2 对于字符串，计算其字符位数
print ( len(b'ABC') ); # 3
print ( len('中文'.encode('utf-8')) ); # 6 对于字节流，计算字节位数

# 当python源文件中出现中文，要用下面的方式声明文件编码方式
'''
#!/usr/bin/env python3          * 通知系统(Linux/OS X)这是一个可以执行的python文件
# -*- coding: utf-8 -*-         * 通知python解释器，按照uft-8编码来读取源文件
'''

# 字符串格式化方法
# %占位符方法 str % ()
''' %s字符串 %d整数 %f浮点数 %x十六进制整数 '''
print('Hello, %s, you are %d years old now' % ('Michael', 30)); # Hello, Michael, you are 30 years old now
print('Number %3d' % (2)); # Number   2 %3d表示: 此处整数占3位，不足则前面补空格' '
print('Number %03d' % (2)); # Number 002 %03d表示: 此整数处占3位，不足则前面补零'0'
print('Float %.2f' % (2.5684)); # Float 2.56 %.2f表示: 此处浮点数只取小数点后两位
print('Percent %d%%' % (80)); # Percent 80% 如果需要用到'%'则用%来转义
# 字符串方法 format()
''' 用 {0} {1:d} {2:.1f} 这样的方式书写 '''
print('Hello, {0}, you are {1:d} years old now'.format('Michael', 30))