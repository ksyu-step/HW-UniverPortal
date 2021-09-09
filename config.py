from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e8ab28febef57d301efec25175788a77'  #
app.config['TEMPLATE_AUTO_RELOAD'] = True
