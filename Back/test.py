from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='GET':
        return render_template('test.html')
    elif request.method=='POST':
        return 'POST'
    

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         print('aaa')
#     else:
#         return render_template('test.html')
#     return 'OK'

if __name__ == '__main__':
    app.run('0.0.0.0')