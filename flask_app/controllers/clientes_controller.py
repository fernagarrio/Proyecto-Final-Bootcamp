from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app
from datetime import datetime 

from flask_app.models.users import User
from flask_app.models.clientes import Clientes

@app.route('/new/cliente')
def new_cliente():
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('new.html')

@app.route('/create/cliente', methods=['POST'])
def create_cliente():
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    if not Clientes.validate_clientes(request.form):
        return redirect('/new/cliente')
    
    
    Clientes.save(request.form)

    return redirect('/dashboard')

@app.route('/edit/cliente/<int:id>') 
def edit_cliente(id):
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    diccionario = {"id": id}
    Cliente = Clientes.get_by_id(diccionario)

    return render_template('edit.html', clientes=Cliente, now=datetime.now )

@app.route('/update/cliente', methods=['POST'])
def update_cliente():
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    

    
    if not Clientes.validate_clientes(request.form):
        return redirect('/edit/cliente/'+request.form['id'])
    
    
    Clientes.update(request.form)
    return redirect('/dashboard')

@app.route('/delete/cliente/<int:id>')
def delete_clientes(id):
    
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    
    form = {"id": id}
    Clientes.delete(form)

    return redirect('/dashboard')