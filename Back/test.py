from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello World2')
    return 'Hello World!'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print('aaa')
    else:
        return render_template('test.html')
    return 'OK'

if __name__ == '__main__':
    app.run()