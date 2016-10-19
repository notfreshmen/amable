from expects import *

from amable.utils.assets import assets_path


with context('amable'):
    with context('utils'):
        with context('assets'):
            with context('assets_path'):
                with it('finds the right directory'):
                    correct_dir = '/amable/utils/../static/css'

                    expect(assets_path('css')).to(contain(correct_dir))
