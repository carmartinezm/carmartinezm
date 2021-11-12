from flask import Flask, request, Response

app = Flask(__name__)



@app.route("/")
def hello():
    user = request.args.get('user')
    password = request.args.get('password')
    if (user == 'atlanticomedio') and (password == '1234'):
        return Response( "BIENVENIDO SEAS A NUESTRA SECTA" , status=200)
    else:
        return Response("TU ACCESO HA SIDO DENEGADO, LA AUTODESTRUCCIÓN COMENZARÁ EN 3, 2, 1... ¡¡¡¡BOOOOOMMMM!!!" , status=401)

if __name__ == '__main__':
     app.run(port='5000')

