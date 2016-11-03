from expects import *

from amable import app

from amable.forms.user_update_form import UserUpdateForm


with context('amable.forms.user_create_form'):
    with context('UserUpdateForm'):
        with context('username'):
            with it('is required'):
                with app.app_context():
                    form = UserUpdateForm()
                    form.validate()

                expect(form.errors['username']).to(contain("This field is required."))

            with it('must be between 3 and 25 characters'):
                with app.app_context():
                    form = UserUpdateForm(username='kk')
                    form.validate()

                expect(form.errors['username']).to(contain("Field must be between 3 and 25 characters long."))

        with context('email'):
            with it('is required'):
                with app.app_context():
                    form = UserUpdateForm()
                    form.validate()

                expect(form.errors['email']).to(contain("This field is required."))

            with it('must be a valid email'):
                with app.app_context():
                    form = UserUpdateForm(email='foobar')
                    form.validate()

                expect(form.errors['email']).to(contain("Invalid email address."))

        with context('name'):
            with it('is required'):
                with app.app_context():
                    form = UserUpdateForm()
                    form.validate()

                expect(form.errors['name']).to(contain("This field is required."))
