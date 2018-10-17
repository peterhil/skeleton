# Load all required libraries.
gulp       = require 'gulp'
accord     = require 'gulp-accord'
sass       = require 'gulp-ruby-sass'
prefix     = require 'gulp-autoprefixer'
cssmin     = require 'gulp-cssmin'
# jade       = require 'gulp-jade'
# minifyHTML = require 'gulp-minify-html'
svgmin     = require 'gulp-svgmin'

gulp.task 'less', ->
  gulp.src 'app/static/style/*.less'
    .pipe accord('less', {pretty: false})
    # .pipe prefix "> 1%"
    # .pipe cssmin keepSpecialComments: 0
    .pipe gulp.dest 'www/style'

# Create your CSS from Sass, Autoprexif it to target 99%
#  of web browsers, minifies it.
gulp.task 'css', ->
  gulp.src 'app/static/style/*.sass'
    .pipe sass()
    # .pipe prefix "> 1%"
    .pipe cssmin keepSpecialComments: 0
    .pipe gulp.dest 'www/css'

# Create you HTML from Jade, Adds an additional step of
#  minification for filters (like markdown) that are not
#  minified by Jade.
# gulp.task 'html', ->
#   gulp.src 'app/index.jade'
#     .pipe jade()
#     .pipe minifyHTML()
#     .pipe gulp.dest 'www'

# Minify your SVG.
gulp.task 'svg', ->
  gulp.src 'app/static/img/*.svg'
    .pipe svgmin()
    .pipe gulp.dest 'www/img'

# Copy the fonts using streams.
gulp.task 'copy', ->
  gulp.src 'app/static/font/*'
    .pipe gulp.dest 'www/font'

# Default task call every tasks created so far.
gulp.task 'default', ['css', 'copy']
