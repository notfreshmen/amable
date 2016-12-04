'use strict'

var gulp = require('gulp')
var sass = require('gulp-sass')
var concat = require('gulp-concat')
var uglify = require('gulp-uglify')
var clean = require('gulp-clean')
var livereload = require('gulp-livereload')

var css_src = './amable/assets/css/**/*.scss'
var css_dest = './amable/static/css/'

var jsc_src = [
  './node_modules/jquery/dist/jquery.js',
  './node_modules/chosen-js/chosen.jquery.js',
  './amable/assets/jsc/**/*.js'
]
var jsc_dest = './amable/static/jsc/'

gulp.task('css_build', function () {
  var options = {
    includePaths: [
      './node_modules/chosen-js',
      './amable/assets/css/lib'
    ],
    outputStyle: 'nested'
  }

  gulp.src(css_src)
      .pipe(sass(options).on('error', sass.logError))
      .pipe(gulp.dest(css_dest))
      .pipe(livereload())
})

gulp.task('css_clean', function() {
  gulp.src(css_dest, { read: false }).pipe(clean())
})

gulp.task('jsc_build', function () {
  gulp.src(jsc_src)
      .pipe(uglify())
      .pipe(concat('application.js'))
      .pipe(gulp.dest(jsc_dest))
      .pipe(livereload())
})

gulp.task('jsc_clean', function () {
  gulp.src(jsc_dest, { read: false }).pipe(clean())
})

gulp.task('css', ['css_clean', 'css_build'])
gulp.task('jsc', ['jsc_clean', 'jsc_build'])

gulp.task('watch', function () {
  livereload.listen();

  gulp.watch(css_src, ['css'])
  gulp.watch(jsc_src, ['jsc'])
})

gulp.task('build', ['css', 'jsc'])


gulp.task('default', ['build'])
