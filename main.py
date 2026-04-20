from flask import Flask 
import random 

app = Flask(__name__)

# Rotas
@app.route('/')
def homepage():
    return 'bem-vindo à homepage, digite "/dado" para começar.'

@app.route('/dado')
def dado():
    rand = random.randint(1, 6)
    return f'Atualize a página. Você tirou: {rand}'

if __name__ == '__main__':
    app.run(debug=True)
