from flask import Flask, render_template, request, send_file
import os
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      passwd = request.form.get('password')
      passwd_arc = request.form.get('passwordarc')
      os.system("rm -r ./tmp/*")
      f.save(f"./tmp/{f.filename}")
      extr_command = f'python3 ./patool/patool extract ./tmp/{f.filename}'
      if (passwd_arc != ""):
         extr_command += f' --password {passwd_arc}'
      extr_command +=  ' --outdir ./tmp'
      errorlevel = os.system(extr_command)
      if errorlevel > 0:
         return f'Неправильный архив или пароль к нему!!!'
      dir_name = os.path.splitext(f.filename)[0]
      print (dir_name)
      out_file = f"./{dir_name}.pem"
      os.system(f"./get-cpcert ./tmp/{dir_name} {passwd}  > {out_file}")
  
      content = open(out_file, 'r').read().replace('\n', '<br>')
      if os.stat(out_file).st_size > 0:
         return f'Файл  {f.filename} загружен <br>  <a href="{out_file}" download> Скачать </a> <br> {content}'
      else:
         return "Не удалось преобразовать файл"

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
#    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#    return send_from_directory( filename=filename)
     return send_file(filename, as_attachment=True)

		
if __name__ == '__main__':
   app.run(debug = True)
