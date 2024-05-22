from flask import render_template
from flask_login import current_user

def patients(users):
    return render_template(
        "patients.html",
        users=users,
        title="Lista de pacientes",
        current_user=current_user,
    )

def create():
    return render_template(
        "create_patients.html", title="Registro de pacientes", current_user=current_user
    )

def update(user):
    return render_template(
        "update_patient.html",
        title="Actualizar paciente",
        user=user,
        current_user=current_user,
    )

def login():
    return render_template(
        "login.html", title="Inicio de sesión", current_user=current_user
    )

def patients(user):
    return render_template(
        "patients.html", title="Perfil de usuario", current_user=current_user, user=user
    )