$(document).ready(function () {
  $('.js-load-more').on('click', function () {
    var button = $(this)
    var feed = $('.dashboard__content__feed')
    var feedType = feed.data('feed')
    var postsContainer = feed.children('section')
    var page = parseInt(button.data('next-page'))
    var url = '/posts.json?feed=' + feedType + '&page=' + page

    button.html('Loading...')

    $.getJSON(url).done(function (data) {
      $.each(data.posts, function (i, post) {
        postsContainer.append(post)
      })

      button.data('next-page', page + 1)
      button.html('Load More')
    })
  })
})
