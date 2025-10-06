from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/done/<int:index>')
def done(index):
    tasks[index]['done'] = True
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)