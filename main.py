from flask import Flask, render_template, request, redirect, url_for
import bd_tabl
import datetime

app = Flask(__name__)
bd_tabl.create_tables()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/list", methods=['POST'])
def add_to_list():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        today = datetime.date.today()
        data = today.strftime("%Y-%m-%d")

        pid = bd_tabl.list_stranichka(name, data, description)
        return redirect(url_for('show_list', pid=pid))


# Отображение базы данных на странице
@app.route("/list", methods=['GET'])
def show_list():
    todos = bd_tabl.get_all_todos()

    return render_template("list.html", todo_items=todos)


# Удаление из базы данных и страницы
@app.route("/delete", methods=['POST'])
def delete_todo():
    if request.method == 'POST':
        delete_id = request.form.get('delete_id')

        if delete_id:
            bd_tabl.delete_todo(delete_id)

    return redirect(url_for('show_list'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
