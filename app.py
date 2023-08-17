from flask import (Flask, render_template, request, session, redirect, url_for, g, abort)

app =Flask(__name__)
app.secret_key='some_sercet_key_that_only_i_should_know'

# chacking is the userid exists in the session
@app.before_request
def before_request():
    g.user=None
    if 'user_id' in session:
        user=[x for x in users if x.id==session['user_id']][0]
        g.user=user
# anywhere that we can use g which is anywhere we'll have access to the user if they're logged in already (its used in the profile.html to display the users name)

class User:
    def __init__(self, id, username, password) -> None:
        self.id=id
        self.username=username
        self.password=password

    def __repr__(self) -> str:
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='Tanu', password='tdk'))
# print(users)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        session.pop('user_id', None)

        username=request.form['username']
        password=request.form['password']

        user=[x for x in users if x.username==username][0]
        if user and user.password==password:
            session['user_id']= user.id
            return redirect(url_for('profile'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        # abort(403)
        return redirect(url_for('login'))
    return render_template('profile.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)








