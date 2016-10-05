from expects import *

from amable.utils.password import hash_password, check_password


with context('amable'):
    with context('utils'):
        with context('password'):
            with context('hash_password'):
                with it('returns a hashed password'):
                    expect(hash_password('foobar')).not_to(equal('foobar'))

            with context('check_password'):
                with it('returns true for correct passwords'):
                    hash = hash_password('foobar')

                    expect(check_password(hash, 'foobar')).to(be_true)

                with it('returns false for incorrect passwords'):
                    hash = hash_password('foobar')

                    expect(check_password(hash, 'barfoo')).to(be_false)
