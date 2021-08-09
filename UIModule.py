from flask import Flask, redirect, url_for, request, render_template, send_file,send_from_directory
#from 'Final_Year_Project/EnumerationModule/BasicScanScript.py' import SCAN
from EnumerationModule.ScanScript import SCAN
from TestingModule.test1 import CVE_SCAN
from report_generation_module import pdfmaker
from TestingModule.web_test_sslyze import SSL_SCAN
from TestingModule.directory_traverse import gobuster_test
import os,subprocess
from webtest_reportmaker import webtest_pdfmaker
app = Flask(__name__)

@app.before_first_request
def _declareStuff():
   subprocess.Popen(['pwd'],universal_newlines=True)



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
      return render_template("web_testing.html",ip_address=".".join(IP.split(":")),filename=output)
      #return "<a href='/download-report/{}' target='_blank'><button>Download final Report</button></a>".format(output)
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
      print(filename)
      return send_from_directory(directory="results", filename=filename,as_attachment=True)
   except Exception as e:
      return str(e)

@app.route('/webtesting',methods=['POST'])
def webtester():
   if request.method == "POST":
      ip = request.form["IP"]
      print(request.form)
      ssl_filename = SSL_SCAN(ip)
      gobuster_filename = gobuster_test(ip)
      webreport = webtest_pdfmaker(":".join(ip.split('.')))
      return "<a href='/download-report/{}' target='_blank'><button>Download final_webtest report</button></a>".format(webreport)

   return render_template('web_testing.html',ip_address="0.0.0.0",filename="0:0:0:0.xml")



if __name__ == '__main__':
   app.run(debug = True)