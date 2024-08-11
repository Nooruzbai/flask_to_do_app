from flask import render_template, Blueprint, redirect, url_for, flash, current_app, jsonify, typing as ft, request, \
    abort
from flask_login import current_user

from source import db
from source.to_do_app.to_do_forms import ToDoForm, ToDoUpdateForm
from source.to_do_app.to_do_models import ToDo

to_do = Blueprint('to_do', __name__)


@to_do.route("/to_dos/", methods=['GET'])
def list_to_dos():
    todos = ToDo.query.all()
    return render_template('list_to_dos.html', todos=todos, user=current_user)

@to_do.route("/to_do/create/", methods=["GET","POST"])
def create_to_do():
    form = ToDoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_todo = ToDo(
                name=form.name.data,
                description=form.description.data,
                due_date=form.due_date.data,
                priority=form.priority.data,
                status=form.status.data,
                user_id=current_user.id
            )
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('to_do.list_to_dos'))
    return render_template('to_do_create.html', user=current_user, form=form)



@to_do.route("/to_do/detail/<int:todo_id>/", methods=['GET'])
def to_do_detail(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    return render_template('to_do_detail.html', todo=todo, user=current_user)


@to_do.route("/to_do/update/<int:todo_id>/", methods=["GET", "POST"])
def to_do_update(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    form = ToDoUpdateForm(obj=todo)
    print(request.method)
    if request.method == "POST":
        if todo.user_id != current_user.id:
            abort(403)
        form = ToDoForm(obj=todo)
        if form.validate_on_submit():
            todo.name = form.name.data
            todo.description = form.description.data
            todo.due_date = form.due_date.data
            todo.priority = form.priority.data
            todo.status = form.status.data
            db.session.commit()
            return redirect(url_for('to_do.list_to_dos'))
    return render_template('to_do_update.html', form=form, todo=todo, user=current_user)


@to_do.route("/to_do/delete/<int:todo_id>/",)
def to_do_delete(todo_id):
    print(request.method)
    todo = ToDo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        abort(403)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('to_do.list_to_dos'))


