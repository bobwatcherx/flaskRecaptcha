from flask import Flask,render_template,request
from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,BooleanField,SubmitField,validators
from wtforms.widgets import HiddenInput

from flask_wtf.recaptcha import RecaptchaField


# CREATE CLASS FOR INPUT FIELD LIKE NAME PASSWORD AND  MORE
class RegisterForm(FlaskForm):
	name = StringField("Name",[validators.DataRequired(),validators.length(max=255)])
	password = PasswordField("Password",[validators.DataRequired(),validators.length(min=8)])
	email = StringField("Email",[validators.DataRequired(),validators.length(min=6,max=35)])
	recaptcha = RecaptchaField()
	submit = SubmitField("Register now")


app = Flask(__name__)
app.config["SECRET_KEY"] = "myrandomomdqwdqwkdnqw"
app.config["RECAPTCHA_USE_SSL"] = False
# THIS GET FROM DASHBOARD

app.config["RECAPTCHA_PUBLIC_KEY"] = "6LdtJgwkAAAAAKWkOpix8uiMNB5xmmv60SuGBIBF"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LdtJgwkAAAAAN8M1EwVEDRWuvd6D1vcTI8iqP1i"
app.config["RECAPTCHA_OPTIONS"] = {'theme':'black'}


@app.route("/register",methods=['GET','POST'])
def register():
	form = RegisterForm()

	# IF THE SUBMIT FORM SUCCESS THEN SEND MESSAGE SUCCESS
	if form.validate_on_submit():
		return "YOu Success send data !!!"

	# THEN RENDER HTML TEMPLATE 
	return render_template("register.html",form=form)


if __name__ == "__main__":
	app.run(port=5000,debug=True)








