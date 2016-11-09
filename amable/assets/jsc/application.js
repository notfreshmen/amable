$(function () {

  // Nav toggle
  $('.header__toggle').on('click', function () {
    var nav = $(this).siblings('.header__nav')

    $(nav).toggleClass('mobile-hidden')
    $(nav).toggleClass('mobile-visible')
  })

  // Communities search
  $('.communities__search input').on('keyup', function() {
    var search = $(this).val().toLowerCase()

    var results = $('.communities__community').filter(function () {
      return $(this).find('h3').html().toLowerCase().includes(search)
    }).toArray()

    $('.communities__community').each(function () {
      if (results.includes(this)) {
        $(this).removeClass('hidden')
        $(this).addClass('visible')
      } else {
        $(this).removeClass('visible')
        $(this).addClass('hidden')
      }
    })
  })
})
