from flask import Flask, redirect, url_for, request, render_template, send_file,send_from_directory
#from 'Final_Year_Project/EnumerationModule/BasicScanScript.py' import SCAN
from EnumerationModule.ScanScript import SCAN
from TestingModule.test1 import CVE_SCAN
from report_generation_module import pdfmaker
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
      filename = SCAN(ip_final)
      return render_template('enumeration_phase.html',filename=filename)

@app.route('/enumeration',methods=['GET','POST'])
def Enumerate():
   if request.method=="POST":
      IP = request.form["ip"]
      print("enumeration,",IP)
      result = CVE_SCAN(IP)
      output = pdfmaker(IP)
      return "<a href='/download-report/{}' target='_blank'><button>Download final Report</button></a>".format(output)
   return render_template('enumeration_phase.html',filename="0:0:0:0")

@app.route('/return-file/<filename>',methods=['post','get'])
def downloadfile(filename):
   try:
      return send_from_directory(directory="cache", filename=filename,as_attachment=True)
   except Exception as e:
      return str(e)

@app.route('/download-report/<filename>',methods=['POST','GET'])
def downloadreport(filename):
   try:
      return send_from_directory(directory="results", filename=filename,as_attachment=True)
   except Exception as e:
      return str(e)


if __name__ == '__main__':
   app.run(debug = True)