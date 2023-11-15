from flask import Flask
from stocks import stocks_blueprint
from test import test_blueprint
from monthlydata import monthly_blueprint
from top30stocks import top30stocks_blueprint
from allstocksdata import allstocksdata_blueprint
from indicator import indicator_blueprint
# form senddata import stock_blueprint

app = Flask(__name__)

# Register the Blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(monthly_blueprint)  
app.register_blueprint(top30stocks_blueprint)
app.register_blueprint(allstocksdata_blueprint)
app.register_blueprint(indicator_blueprint)
# app.register_blueprint(stock_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
