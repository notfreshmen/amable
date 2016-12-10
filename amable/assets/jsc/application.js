$(function () {
  // Chosen
  $('.chosen').chosen()

  // Nav toggle
  $('.header__toggle').on('click', function () {
    var nav = $(this).siblings('.header__nav')

    $(nav).toggleClass('mobile-hidden')
    $(nav).toggleClass('mobile-visible')
  })

  // Communities search
  $('.communities__search input').on('keyup', function () {
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

  // Communities vote
  $('.js-community-vote').on('click', function () {
    var button = $(this)
    var id = button.data('id')

    $.getJSON('/communities/' + id + '/vote', function (data) {
      button.removeClass('btn--blue')

      if (data.success) {
        button.html('Voted')
        button.attr('disabled', '')
      } else {
        button.addClass('btn--red')
        button.html('Error!')
      }
    })
  })

  // Communities membership
  $('.js-community-membership').on('click', function () {
    var button = $(this)
    var id = button.data('id')

    $.getJSON('/communities/' + id + '/membership', function (data) {
      if (data.action === 'joined') {
        button.removeClass('btn--blue')
        button.addClass('btn--red')
        button.html('Leave')
      } else if (data.action === 'left') {
        button.removeClass('btn--red')
        button.addClass('btn--blue')
        button.html('Join')
      }
    })
  })

  $('.post_upvote').click(function (r) {
    r.preventDefault()
    var postID = this.id.split('_')[2]
    var alreadyUpvoted = $('#upvote_icon_' + postID).css('color') === 'rgb(0, 128, 0)' // Already green
    var currentUpvotes = $('#upvote_number_' + postID).html()
    // If the post is already we want to then downvote it
    if (!alreadyUpvoted) { // Upvote
      $.getJSON('/posts/' + postID + '/upvote', function (data) {
        if (data.success) {
          $('#upvote_number_' + postID).html(parseInt(currentUpvotes, 10) + 1)
          $('#upvote_icon_' + postID).css('color', 'green')
        } else {
          $('#upvote_icon_' + postID).css('color', 'red')
        }
      })
    } else { // Downvote
      $.getJSON('/posts/' + postID + '/downvote', function (data) {
        if (data.success) {
          $('#upvote_number_' + postID).html(parseInt(currentUpvotes, 10) - 1)
          $('#upvote_icon_' + postID).css('color', '')
        } else {
          $('#upvote_icon_' + postID).css('color', 'red')
        }
      })
    }
  })

  $('.reply_comment').click(function (r) {
    // Don't scroll to top of screen
    r.preventDefault()

    // Get the target of the click (element)
    var clickedElement = r.target
    var formElement = $('#reply_to_comment_' + clickedElement.id.split('_')[2] + '_form')

    // Lets create our form!
    if (formElement.is(':visible')) {
      formElement.hide()
    } else {
      formElement.show()
    }
  })

  $('.js-toggle-post-comment').click(function (e) {
    e.preventDefault()

    var postID = $(this).data('post-id')
    var form = $('form[data-post-id="' + postID + '"][data-action="comment"]')

    if (form.is(':visible')) {
      form.hide()
    } else {
      form.show()
    }
  })

  $('.js-toggle-post-report').click(function (e) {
    e.preventDefault()

    var postID = $(this).data('post-id')
    // var form = $('#report_post_' + clickedElement.id.split('_')[2] + '_form')
    var form = $('form[data-post-id="' + postID + '"][data-action="report"]')

    // Lets create our form!
    if (form.is(':visible')) {
      form.hide()
    } else {
      form.show()
    }
  })

  $('.follow_user').click(function (r) {
    r.preventDefault()

    var clickedElement = r.target
    var buttonCheck = clickedElement.id.match(/unfollow_*/)

    if (buttonCheck == null) {
      $.getJSON('/follow/' + clickedElement.id.split('_')[1], function (data) {
        if (data.success) {
          clickedElement.innerHTML = 'Unfollow'
        } else {
          console.error('Unable to follow user')
        }
      })
    } else {
      $.getJSON('/unfollow/' + clickedElement.id.split('_')[1], function (data) {
        if (data.success) {
          clickedElement.innerHTML = 'Follow'
        } else {
          console.error('Unable to unfollow user')
        }
      })
    }
  })

  // Dashboard filters
  $('.filter__community').on('change', function () {
    var selected = $.map($(this).children('option:selected'), function (option) {
      return $(option).attr('value')
    })

    var ids = selected.join(',')

    if (ids.length === 0) {
      window.location.href = '/'
    } else {
      window.location.href = '/?communities=' + ids
    }
  })

  // Post form
  $('.dashboard__form textarea').on('focus', function () {
    $(this).addClass('expanded')
    $(this).parent().siblings('.form__group--footer').removeClass('hidden')
  }).on('blur', function () {
    $(this).removeClass('expanded')
    $(this).parent().siblings('.form__group--footer').addClass('hidden')
  })
})
