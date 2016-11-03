from expects import *

from amable import app

from amable.forms.user_create_form import UserCreateForm


with context('amable.forms.user_create_form'):
    with context('UserCreateForm'):
        with context('username'):
            with it('is required'):
                with app.app_context():
                    form = UserCreateForm()
                    form.validate()

                expect(form.errors['username']).to(contain("This field is required."))

            with it('must be between 3 and 25 characters'):
                with app.app_context():
                    form = UserCreateForm(username='kk')
                    form.validate()

                expect(form.errors['username']).to(contain("Field must be between 3 and 25 characters long."))

        with context('email'):
            with it('is required'):
                with app.app_context():
                    form = UserCreateForm()
                    form.validate()

                expect(form.errors['email']).to(contain("This field is required."))

            with it('must be a valid email'):
                with app.app_context():
                    form = UserCreateForm(email='foobar')
                    form.validate()

                expect(form.errors['email']).to(contain("Invalid email address."))

        with context('name'):
            with it('is required'):
                with app.app_context():
                    form = UserCreateForm()
                    form.validate()

                expect(form.errors['name']).to(contain("This field is required."))

        with context('password'):
            with it('is required'):
                with app.app_context():
                    form = UserCreateForm()
                    form.validate()

                expect(form.errors['password']).to(contain("This field is required."))

            with it('must match password_confirmation'):
                with app.app_context():
                    form = UserCreateForm(password='foobar', password_confirmation='barfoo')
                    form.validate()

                expect(form.errors['password']).to(contain("Passwords must match."))

        with context('password_confirmation'):
            with it('is required'):
                with app.app_context():
                    form = UserCreateForm()
                    form.validate()

                expect(form.errors['email']).to(contain("This field is required."))
