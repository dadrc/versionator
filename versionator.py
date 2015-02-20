#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import imp
from os import path, listdir
import sqlite3

plugin_folder = "./plugins"
module = "__init__"
debug = True


def get_products():
    products = []
    con = sqlite3.connect('versionator.db')
    c = con.cursor()
    c.execute('SELECT product_id, name, module FROM products')
    for row in c:
        products.append(row)
    con.close()
    return products


def load_plugins(products):
    instances = {}
    for product in products:
        l = path.join(plugin_folder, product[2])
        if not path.isdir(l) or not module + '.py' in listdir(l):
            continue
        info = imp.find_module(module, [l])
        instances[product[0]] = imp.load_module(module, *info)
    return instances


products = get_products()
instances = load_plugins(products)
for plugin in instances.values():
    plugin.hello()
    #plugin.run()
