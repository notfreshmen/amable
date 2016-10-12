from expects import *

from amable.utils.assets import assets_path, node_modules_path, sass_filter


with context('amable'):
    with context('utils'):
        with context('assets'):
            with context('assets_path'):
                with it('finds the right directory'):
                    correct_dir = '/amable/utils/../assets/css'

                    expect(assets_path('css')).to(contain(correct_dir))

            with context('node_modules_path'):
                with it('finds the right directory'):
                    correct_dir = '/amable/utils/../../node_modules/jquery'

                    expect(node_modules_path('jquery')).to(contain(correct_dir))

            with context('sass_filter'):
                with _it('takes SCSS from stdin and outputs CSS to stdout'):
                    pass
