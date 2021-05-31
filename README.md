# get_pem2

flask shell for usage converter crypto pro key to openssl via web

You must first install project https://github.com/kov-serg/get-cpcert

After you can usage this webform for work.

You must archive folder of crypto pro container <keyname.000> to zip, 7z file and upload to webform. additionaly please enter password of crypocontainer.
flask app extract file and convert to pem format with get-cpcert utility and patool.


You can use image form dockerhub
https://hub.docker.com/r/jora450000/get_pem2

You can easy run docker and enjoy:
docker run -p 80:5000 jora450000/get_pem2
