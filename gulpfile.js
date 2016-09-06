var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function() {
  gulp.src('psn/assets/css/**/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(gulp.dest('./static/css/'))
});

gulp.task('watch', function() {
  gulp.watch('psn/assets/css/**/*.scss', ['sass'])
});

gulp.task('build', ['sass'])

gulp.task('default', ['build']);
