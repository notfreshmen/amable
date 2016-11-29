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
    var current_upvotes = $('#upvote_number_' + postID).html()
    // If the post is already we want to then downvote it
    if (!alreadyUpvoted) { // Upvote
      $.getJSON('/posts/' + postID + '/upvote', function(data) {
        if (data.success) {
          $('#upvote_number_' + postID).html(parseInt(current_upvotes, 10) + 1)
          $('#upvote_icon_' + postID).css('color', 'green')
        } else {
          $('#upvote_icon_' + postID).css('color', 'red')
        }
      })
    } else { // Downvote
      $.getJSON('/posts/' + postID + '/downvote', function(data) {
        if (data.success) {
          $('#upvote_number_' + postID).html(parseInt(current_upvotes, 10) - 1)
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

    // Lets create our form!

    $('#reply_to_comment_' + clickedElement.id.split('_')[2] + '_form').show()
    // if ($("#newCommentForm_" + clickedElement.id).length == 0) { // Only create form if it doesn't exist
    //   $("#" + clickedElement.id).after('<form id="newCommentForm_' + clickedElement.id + '" action="/comments/new" method="POST">')
    //   $("#newCommentForm_" + clickedElement.id).append('<input name="parent" type="hidden" value="' + clickedElement.id.split('_')[2] + '">')
    //   $("#newCommentForm_" + clickedElement.id).append('<textarea name="content" form="newCommentForm"></textarea>')
    //   $("#newCommentForm_" + clickedElement.id).append('<input type="submit" value="Reply To Comment">')
    // }
    

    // clickedElement.after('<form action="/comments/new" method="POST">')
    // clickedElement.after('</form>')

    // var commentTextArea = document.createElement("TEXTAREA")
    
    // alert(clickedElement.id)
    // // commentTextArea.id = 'new_comment_' + r.id
    // // clickedElement.closest('li').after(commentTextArea)
    // clickedElement.after(commentTextArea)
  })
})




