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
    # If the item name exists in the DB:
    if item:
        name = item[1]
        price = item[2]
        picture = item[3]
        return render_template("item.html", \
                                name=name, \
                                price=price, \
                                picture=picture)
    # If the item name does not exist in the DB:
    else:
        return render_template("item-not-found.html")