from flask import Flask
app =  Flask(__name__)

from basic.views import basic_blueprint
from sheet_ajax.views import sheet_ajax_blueprint


####################
#### blueprints ####
####################

app.register_blueprint(basic_blueprint)
app.register_blueprint(sheet_ajax_blueprint)
