import os
from flask.views import View, MethodView

from flask import render_template, Blueprint, redirect, url_for, flash, current_app, jsonify, typing as ft, request, \
    abort
from flask_login import current_user

from source import db
from source.to_do_app.to_do_forms import ToDoForm
from source.to_do_app.to_do_models import ToDo

to_do = Blueprint('to_do', __name__)


to_do.route("/to_dos/")
def list_todos():
    todos = ToDo.query.all()
    return render_template('list_to_dos.html', todos=todos, user=current_user)





# class RetriveCreateToDOView(View):
#     methods = ["GET", "POST"]
#
#     def get(self, todo_id=None):
#         if todo_id is None:
#             form = ToDoForm()  # Create an instance of the form
#             return render_template('to_do_create.html', form=form, user=current_user)
#         todo = ToDo.query.get_or_404(todo_id)
#         return render_template('to_do_detail.html', todo=todo, user=current_user)

#     def post(self):
#         form = ToDoForm()
#         if form.validate_on_submit():
#             new_todo = ToDo(
#                 name=form.name.data,
#                 description=form.description.data,
#                 due_date=form.due_date.data,
#                 priority=form.priority.data,
#                 status=form.status.data,
#                 user_id=current_user.id
#             )
#             db.session.add(new_todo)
#             db.session.commit()
#             return redirect(url_for('to_do.index'))
#         return render_template('to_do_create.html', form=form)
#
#     def dispatch_request(self):
#         if request.method == "GET":
#             return self.get()
#         if request.method == "POST":
#             return self.post()
#
# to_do.add_url_rule("/create-todo", view_func=RetriveCreateToDOView.as_view("create_to_do"))




# class RetriveDetailUpdateToDoView(View):
#     def get(self, todo_id):
#         todo = ToDo.query.get_or_404(todo_id)
#         return render_template('to_do_detail.html', todo=todo, user=current_user)
#
#
#
# to_do.add_url_rule("/todo/<int:todo_id>", view_func=RetriveDetailUpdateToDoView.as_view("detail_todo"))


#
# class ToDoCRUDView(MethodView):
#     def get(self, todo_id=None):
#         if todo_id is None:
#             form = ToDoForm()  # Create an instance of the form
#             return render_template('to_do_create.html', form=form, user=current_user)
#         todo = ToDo.query.get_or_404(todo_id)
#         return render_template('to_do_detail.html', todo=todo, user=current_user)
#
#     def post(self):
#         form = ToDoForm()
#         if form.validate_on_submit():
#             new_todo = ToDo(
#                 name=form.name.data,
#                 description=form.description.data,
#                 due_date=form.due_date.data,
#                 priority=form.priority.data,
#                 status=form.status.data,
#                 user_id=current_user.id
#             )
#             db.session.add(new_todo)
#             db.session.commit()
#             return redirect(url_for('to_do.index'))
#         return render_template('to_do_create.html', form=form)

#     def put(self, todo_id):
#         todo = ToDo.query.get_or_404(todo_id)
#         if todo.user_id != current_user.id:
#             abort(403)
#         form = ToDoForm(obj=todo)
#         if form.validate_on_submit():
#             todo.name = form.name.data
#             todo.description = form.description.data
#             todo.due_date = form.due_date.data
#             todo.priority = form.priority.data
#             todo.status = form.status.data
#             db.session.commit()
#             return redirect(url_for('to_do.index'))
#         return render_template('to_do_update.html', form=form, todo=todo)
#
#     def delete(self, todo_id):
#         todo = ToDo.query.get_or_404(todo_id)
#         if todo.user_id != current_user.id:
#             abort(403)
#         db.session.delete(todo)
#         db.session.commit()
#         return redirect(url_for('to_do.index'))
#
#
# # to_do.add_url_rule("/todo/<int:todo_id>", view_func=ToDoCRUDView.as_view("detail_todo"))
# to_do.add_url_rule("/todo/<int:todo_id>", view_func=ToDoCRUDView.as_view("update_todo"))
# to_do.add_url_rule("/delete-todo/<int:todo_id>", view_func=ToDoCRUDView.as_view("delete_to_do"), methods=['DELETE'])
