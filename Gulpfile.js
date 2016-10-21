'use strict'

var gulp = require('gulp')
var sass = require('gulp-sass')
var concat = require('gulp-concat')
var uglify = require('gulp-uglify')

var css_src = './amable/assets/css/**/*.scss'
var jsc_src = [
  './node_modules/jquery/dist/jquery.js',
  './amable/assets/jsc/**/*.js'
]

gulp.task('css', function () {
  var dest = './amable/static/css/'
  var options = {
    includePaths: [
      './amable/assets/css/lib'
    ],
    outputStyle: 'compressed'
  }

  gulp.src(css_src)
      .pipe(sass(options).on('error', sass.logError))
      .pipe(gulp.dest(dest))
})

gulp.task('jsc', function () {
  var dest = './amable/static/jsc/'

  gulp.src(jsc_src)
      .pipe(uglify())
      .pipe(concat('application.js'))
      .pipe(gulp.dest(dest))
})

gulp.task('watch', function () {
  gulp.watch(css_src, ['css'])
  gulp.watch(jsc_src, ['jsc'])
})

gulp.task('build', ['css', 'jsc'])

gulp.task('default', ['build'])
