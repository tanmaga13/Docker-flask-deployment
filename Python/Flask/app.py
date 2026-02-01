from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def Home():
    return "Hello Everyone! This is my first server using Flask"

@app.route('/secend')
def secend():
    return "Hello Shawty! This is my sexond page!"
    
'''
@app.route('/api/<a>/<b>')
def action(a,b):
    result = int(a) + int(b)
    return {               # we cannot return answer in form of integer, it should str/tuple/dict,etc
        'ans': result
    } 
'''

@app.route('/api')
def name():
    name = request.values.get('name')  #/api?name=Tanmay&age=25
    age = request.values.get('age')

    result = {
        'name': name,
        'age': age
    }
    return result

if __name__ == '__main__':
    app.run(debug=True)

