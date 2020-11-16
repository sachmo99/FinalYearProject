from flask import Flask, redirect, url_for, request, render_template
#from 'Final_Year_Project/EnumerationModule/BasicScanScript.py' import SCAN
from EnumerationModule.BasicScanScript import SCAN
app = Flask(__name__)

@app.route('/')
def Home():
   return render_template('Form.html')


@app.route('/success/<ip>')
def send(ip):
   return 'welcome %s' % ip

@app.route('/Proceed',methods = ['POST'])
def Proceed():
   if request.method == 'POST':
      IP = request.form['IP']
      print(request.form)
      range_choice = request.form['range']
      if(range_choice == "single"):
         ip_final = IP
      else:
         ip_final = IP+"/"+request.form['range_val']
         
      return "WELCOME ASSHOLE " + ip_final

if __name__ == '__main__':
   app.run(debug = True)