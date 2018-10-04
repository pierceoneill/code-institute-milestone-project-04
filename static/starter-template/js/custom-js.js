$(document).ready(function() {

    // Rating Stars Functionality and POST
    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars button').on('mouseover', function() {
        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
    
        // Now highbuttonght all the stars that's not after the current hovered star
        $(this).parent().children('button.star').each(function(e) {
            if (e < onStar) {
                $(this).addClass('hover');
            }
            else {
                $(this).removeClass('hover');
            }
        });
    
    }).on('mouseout', function() {
        $(this).parent().children('button.star').each(function(e) {
            $(this).removeClass('hover');
        });
    });


    /* 2. Action to perform on click */
    $('#stars button').on('click', function() {
        // Getting rating - START
        var formStarUrl = $(this).data('url');
        console.log('formStarUrl: ', formStarUrl);
        // Getting rating - END
        var onStar = parseInt($(this).data('value'), 10); // The star currently selected
        var stars = $(this).parent().children('button.star');
        
        for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
        }
        
        for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
        }
        
        // JUST RESPONSE (Not needed)
        var recipe_rating = parseInt($('#stars button.selected').last().data('value'), 10);
        var msg = "";
        msg = "Thanks! You rated this " + recipe_rating + " stars.";
        responseMessage(msg);
        console.log('recipe_rating: ', recipe_rating);
        
        // POST rating with AJAX
        // This will take care of the POST for the rating stars
        $.ajax({
            url: formStarUrl,
            data: JSON.stringify({ recipe_rating }, null, '\t'),
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                console.log('success. Return does nothing', response);
            },
            error: function(error) {
                console.log('error', error);
            }
        });
    });


    function responseMessage(msg) {
        $('.success-box').fadeIn(200);
        $('.success-box p.text-message').html("<span>" + msg + "</span>");
    }
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems, options);
  });
  
  $(document).ready(function(){
  
  /* 1. Visualizing things on Hover - See next part for action on click */
  $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
   
    // Now highlight all the stars that's not after the current hovered star
    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });
    
  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });
  
  
  /* 2. Action to perform on click */
  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    var stars = $(this).parent().children('li.star');
    
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass('selected');
    }
    
    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass('selected');
    }
    
    // JUST RESPONSE (Not needed)
    var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
    var msg = "";
    if (ratingValue > 1) {
        msg = "Thanks! You rated this " + ratingValue + " stars.";
    }
    else {
        msg = "We will improve ourselves. You rated this " + ratingValue + " stars.";
    }
    responseMessage(msg);
    
  });
  
  
});


function responseMessage(msg) {
  $('.success-box').fadeIn(200);  
  $('.success-box div.text-message').html("<span>" + msg + "</span>");
}

});