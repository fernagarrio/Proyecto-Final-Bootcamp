from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app
from datetime import datetime 

from flask_app.models.users import User
from flask_app.models.ost import Ost

@app.route('/new/ost/<int:clid>')
def new_ost(clid):
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('new_ost.html', clid=clid)

@app.route('/create/ost', methods=['POST'])
def create_ost():
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    if not Ost.validate_ost(request.form):
        return redirect('/new/ost')
    
    Ost.save(request.form)

    idcli = session['idcli']
    return redirect('/dashboardost/'+ str(idcli))

@app.route('/edit/ost/<int:id>') 
def edit_ost(id):
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    diccionario = {"id": id}
    OSt = Ost.get_by_id(diccionario)

    return render_template('edit_ost.html', ost=OSt)

@app.route('/update/ost', methods=['POST'])
def update_ost():
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    if not Ost.validate_ost(request.form):
        return redirect('/edit/ost/'+request.form['id'])
    
    
    Ost.update(request.form)

    idcli = session['idcli']
    return redirect('/dashboardost/'+ str(idcli))

@app.route('/delete/ost/<int:id>')
def delete_ost(id):
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    form = {"id": id}
    Ost.delete(form)

    idcli = session['idcli']
    return redirect('/dashboardost/'+ str(idcli))
