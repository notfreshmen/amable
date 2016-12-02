$(function () {
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

  $('.community_vote').click(function () {
    var communityID = this.id.split('_')[1]
    $.getJSON('/communities/' + communityID + '/vote', function (data) {
      if (data.success) {
        $('#vote_span_' + communityID).html('You voted!')
      } else {
        $('#vote_span_' + communityID).html('oh well')
      }
    })
  })

  $('.post_upvote').click(function () {
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

  $('.reply_post').click(function (r) {
    // Don't scroll to top of screen
    r.preventDefault()

    // Get the target of the click (element)
    var clickedElement = r.target
    var formElement = $('#reply_to_post_' + clickedElement.id.split('_')[3] + '_form')

    // Lets create our form!
    if (formElement.is(':visible')) {
      formElement.hide()
    } else {
      formElement.show()
    }
  })

  $('.report_post').click(function (r) {
    // Don't scroll to top of screen
    r.preventDefault()

    // Get the target of the click (element)
    var clickedElement = r.target
    var formElement = $('#report_post_' + clickedElement.id.split('_')[2] + '_form')

    // Lets create our form!
    if (formElement.is(':visible')) {
      formElement.hide()
    } else {
      formElement.show()
    }
  })

  $('.follow_user').click(function(r) {
    r.preventDefault()

    var clickedElement = r.target
    $.getJSON('/follow/' + clickedElement.id.split('_')[1], function(data) {
      if (data.success) {
        clickedElement.disabled=true
      } else {
        console.error('Unable to follow user')
      }
    }) 
  })
})

