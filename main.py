from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

Exam=[
  { 'question': ' પ્રત્યાયન દરમિયાન સેન્ડર નીચેનામાંથી કયું કાર્ય કરે છે',
'op1': 'સ્વીકાર','op2':' સંકેતન','op3':' પ્રતિપોષણ','op4': 'વિસંકેતન'},
  { 'question': 'પ્રત્યાયન એક  કેવી પ્રક્રિયા છે?',
'op1': '  ત્રીધ્રુવ ','op2':' દ્વિધ્રુવીય','op3':' ચતુર ધ્રુવીય','op4': 'અચલ'}]

@app.route('/')
def hello_world():
  return render_template('index.html',exam=Exam)
  
@app.route('/api')
def list_quiz():
  return jsonify(Exam)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)