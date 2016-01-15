# onelifeatatime
Django website to count dialogues in faith for SGI members, based on district.

How to setup Virtual Host on Ubuntu:

The project is kept under /home/ubuntu/onelifeatatime.in folder. 


The contents of /etc/apache2/sites-enabled/onelifeatatime.in.conf is:

$ cat onelifeatatime.in.conf
<VirtualHost *:80>

    ServerName www.onelifeatatime.in
    ServerAlias onelifeatatime.in
    ServerAdmin webmaster@onelifeatatime.in

    DocumentRoot /home/ubuntu/onelifeatatime.in/dialoguesforpeace

	Alias /static/ /home/ubuntu/onelifeatatime.in/dialoguesforpeace/static/

	<Directory /home/ubuntu/onelifeatatime.in/dialoguesforpeace/static/*>
	    Require all granted
	</Directory>
	WSGIDaemonProcess onelifeatatime python-path=/home/ubuntu/onelifeatatime.in/dialoguesforpeace
    	WSGIProcessGroup onelifeatatime

	WSGIScriptAlias / /home/ubuntu/onelifeatatime.in/dialoguesforpeace/dialoguesforpeace/wsgi.py
	<Directory /home/ubuntu/onelifeatatime.in/dialoguesforpeace>
	    <Files wsgi.py>
		Order deny,allow
		Require all granted
	    </Files>
	</Directory>


</VirtualHost>
