# get_pem2

Flask webform for usage get-cpcert https://github.com/kov-serg/get-cpcert converter from CryptoPro key to openssl .pem 
Please archive folder of CryptPro container <keyname.XXX> to zip, 7z file and upload to webform. For a successful convert of the password-protected container please enter the password in this web-form.

This flask app extract a file and convert to .pem format.


Also you can run its with https://hub.docker.com/r/jora450000/get_pem2



Easy sample:

docker run -p 80:5000 jora450000/get_pem2


Конвертер крипто про ключей в .pem. поддерживаются всевозможные форматы архивов с контейнерами, защищенные паролями, пытается найти ключ во всех папках в архиве. на выходе выплевывается ключ в браузер, есть возможность скачать .pem

кому не хочется пилить окружение - приглашаю в docker:

docker run -p 80:5000 jora450000/get_pem2


