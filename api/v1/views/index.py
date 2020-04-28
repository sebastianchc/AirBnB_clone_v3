#!/usr/bin/python3
from flask import Flask, jsonify, make_response
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    return jsonify({"status": "OK"})
