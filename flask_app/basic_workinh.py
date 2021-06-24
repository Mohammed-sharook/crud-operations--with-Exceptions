from flask import Flask, request, jsonify, abort
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9944394985'
app.config['MYSQL_DB'] = 'crud'

db = MySQL(app)


@app.route("/")
def home_page():
    return "<h1>Home page</h1>"


@app.route('/detail/<int:user_id>')
def details(user_id):
    cursor = db.connection.cursor()
    cursor.execute("select * from users where user_id=%s", (user_id,))
    result = cursor.fetchone()
    return jsonify(result)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    try:
        if request.method == 'POST':
            income_data = request.get_json()
            email = income_data['email']
            name = income_data['name']
            my_cursor = db.connection.cursor()
            my_cursor.execute("insert into users(user_name,user_email) values(%s,%s)", (name, email))
            db.connection.commit()
            my_cursor.close()
            return jsonify('user added successfully')
    except TypeError:
        return jsonify({"exception": "TypeError",
                        "email": None,
                        "name": None
                        })

    except KeyError:
        return jsonify({"Exception": "KeyError"})


@app.route("/update/<int:user_id>", methods=['PUT'])
def update(user_id):
    try:
        if request.method == "PUT":
            income_data = request.get_json()
            email = income_data['email']
            cursor = db.connection.cursor()
            cursor.execute("update users set user_email=%s where user_id = %s", (email,user_id))
            db.connection.commit()
            cursor.close()
            return jsonify("Email changed for user {}".format(user_id))

    except KeyError:
        return jsonify({"keyError":'email'})

    except TypeError:
        return jsonify({"exception": "TypeError",
                        "email": None,
                        "name": None
                        })


@app.route('/delete/<int:user_id>', methods=["DELETE"])
def delete(user_id):
    if request.method == "DELETE":
        cursor = db.connection.cursor()
        cursor.execute("delete from users where user_id = %s", (user_id,))
        db.connection.commit()
        cursor.close()
        return jsonify({'deleted_user_id': user_id})


@app.errorhandler(404)
def error_handler(e):
    return jsonify({"exception": "URL not exists", "status": 404})


if __name__ == '__main__':
    app.run(debug=True)