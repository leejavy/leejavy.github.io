#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-28 19:43:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# __*__ coding: utf-8 __*__
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import argparse
import time

parse = argparse.ArgumentParser()
parse.add_argument("content")
args = parse.parse_args()

times = time.strftime('%Y-%m-%d',time.localtime(time.time()))
content = args.content

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = "javylee@163.com"
password = "06317396883"
to_addr = "jianwei.li@hpe.com"
cc_addr = "javy-lee@163.com"
smtp_server = "smtp.163.com"

msg = MIMEText(content,'html','utf-8')
msg['From'] = _format_addr(u'JavyLee <%s>' % from_addr)
msg['To'] = _format_addr(u'lijianw <%s>' % to_addr)
msg['Subject'] = Header(u'[Daily Report-]'+times,'utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr,cc_addr],msg.as_string())
server.quit()










