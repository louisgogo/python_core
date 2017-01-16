from ftplib import FTP
f = FTP('ftp.cc.ac.cn')
f.login('anonymous', 'guido@python.org')
f.dir()
