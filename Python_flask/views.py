from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    hobby = args.get('hobby')
    return render_template("profile.html", name=name, hobby=hobby)


@views.route("/json")
def get_json():
    return jsonify({'name': 'Akhil', 'age': 23})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


@views.route("/new")
def new_page():
    return render_template("new.html")
