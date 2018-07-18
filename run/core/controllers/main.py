#!/usr/bin/env python3


from flask import Blueprint, redirect, render_template, request, url_for

from core.models import model


controller = Blueprint("main", __name__)


@controller.route("/", methods=["GET"])
def show_index():
    return render_template("index.html")

@controller.route("/<item_name>", methods=["GET"])
def show_item(item_name):
    item = model.get_item_data(item_name)
    name = item[0]
    price = item[1]
    picture = item[2]
    return render_template("item.html", \
                            name=name, \
                            price=price, \
                            picture=picture)