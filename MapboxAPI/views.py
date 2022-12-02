from flask import Blueprint, render_template,request,jsonify,redirect,url_for

views = Blueprint(__name__, 'views')

# This is called the decorators
@views.route("/")
def Location():
    return render_template("mapbox.html",name="  These are location in your area for rock climbing")

@views.route('/about')
def about_page():
    return '<h1>About Page</h1>'
# URL Parameter
@views.route("/profile/")
def profile():
# Query Parameters
    args = request.args
    name = args.get('name','age')
    return render_template("mapbox.html", name='Perry')
#Return JSON
@views.route("/json")
def get_json():
    return jsonify({'name':'Perry','Eagles':'fan', 'SuperBowl:':2017})

#Getting Json Data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#Redirect
@views.route("go-to-home")
def go_to_home():
    return redirect(url_for("views.Location"))


