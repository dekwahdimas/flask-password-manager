from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import PassManager
from web_app.scripts.aes_encryption import encrypter, decrypter
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/about')
def about():
    return render_template("about.html", user=current_user)


@views.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
    if request.method == 'POST': # get the data from the HTML 
        category = request.form.get('category')
        platform = request.form.get('platform')
        add_email = request.form.get('add_email')
        add_pass = request.form.get('add_pass')
        enc_key = request.form.get('enc_key')
        add_pass = encrypter(add_pass, enc_key) # encrypt the password

        if len(category) < 1:
            flash('Category is too short!', category='error') 
        elif len(platform) < 1:
            flash('Platform name is too short!', category='error') 
        else:
            new_pass = PassManager(
                category=category, 
                platform=platform, 
                add_email=add_email, 
                add_pass=add_pass,
                user_id=current_user.id
            ) # providing the schema for the password 
            db.session.add(new_pass) # adding the data to the database 
            db.session.commit()

            flash('Password added!', category='success')

    return render_template("manage.html", user=current_user)


@views.route('/decrypt_password/<int:pass_id>', methods=['POST'])
@login_required
def decrypt_password(pass_id):
    pass_data = PassManager.query.get(pass_id)

    if pass_data and pass_data.user_id == current_user.id:
        data = request.get_json()
        enc_key = data.get('enc_key')
        decrypted_pass = None

        if enc_key:
            try:
                decrypted_pass = decrypter(pass_data.add_pass, enc_key)  # Decrypt the password
                decrypted_pass = decrypted_pass.decode("utf-8") # decode password from bytes to string
                return jsonify(success=True, decrypted_pass=decrypted_pass)
            except Exception as e:
                return jsonify(success=False, message='Incorrect encryption key!')
        else:
            return jsonify(success=False, message='Encryption key is required!')

    return jsonify(success=False, message='Unauthorized or password not found!')


@views.route('/edit_pass/<int:pass_id>', methods=['POST'])
@login_required
def edit_pass(pass_id):
    pass_data = PassManager.query.get(pass_id)

    if pass_data and pass_data.user_id == current_user.id:
        category = request.form.get('category')
        platform = request.form.get('platform')
        add_email = request.form.get('add_email')
        add_pass = request.form.get('add_pass')
        enc_key = request.form.get('enc_key')

        if enc_key:
            add_pass = encrypter(add_pass, enc_key)

        pass_data.category = category
        pass_data.platform = platform
        pass_data.add_email = add_email
        pass_data.add_pass = add_pass

        db.session.commit()
        flash('Password updated!', category='success')
    else:
        flash('Unauthorized or password not found!', category='error')

    return redirect(url_for('views.manage'))


@views.route('/delete-password', methods=['POST'])
def delete_note():
    pass_data = json.loads(request.data)
    pass_dataId = pass_data['pass_dataId']
    pass_data = PassManager.query.get(pass_dataId)
    if pass_data:
        if pass_data.user_id == current_user.id:
            db.session.delete(pass_data)
            db.session.commit()

    return jsonify({})