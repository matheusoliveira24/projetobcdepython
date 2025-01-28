from flask import Flask, render_template

app = Flask(__name__)
@app.route("/olaa")
def home():
   return render_template("nome.html")

@app.route("/ola")
def hello_world():
   return"<p>Olá, Mundo!</p>"

#from modelos.avengers import Avengers
#from modelos.interface import Interface as i
#from modelos.database import Database


#def main():

   Avengers.carregar_herois()
   i.apresentar_menu_principal()

#if __name__ == '__main__': # sempre no final do arquivo contendo a definição da função principal
#    main()