#!/usr/bin/env python3


from flask import Flask

from core.controllers.main import controller as main


# Creates a new Flask web app.
omnibus = Flask(__name__)

# Registers blueprint of the controller for the web app.
omnibus.register_blueprint(main)

# Enables debug mode.
omnibus.config["DEBUG"] = True