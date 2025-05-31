from flask import Flask, render_template, request, redirect, url_for
from models.soal import db, Soal
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def index():
    tingkat = request.args.get('tingkat')
    if tingkat:
        soals = Soal.query.filter_by(tingkat=tingkat).all()
    else:
        soals = Soal.query.all()
    return render_template('list_soal.html', soals=soals)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        soal = Soal(
            pertanyaan=request.form['pertanyaan'],
            jawaban=request.form['jawaban'],
            tingkat=request.form['tingkat']
        )
        db.session.add(soal)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form_soal.html', action='Tambah')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    soal = Soal.query.get_or_404(id)
    if request.method == 'POST':
        soal.pertanyaan = request.form['pertanyaan']
        soal.jawaban = request.form['jawaban']
        soal.tingkat = request.form['tingkat']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form_soal.html', soal=soal, action='Edit')

@app.route('/hapus/<int:id>')
def hapus(id):
    soal = Soal.query.get_or_404(id)
    db.session.delete(soal)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
