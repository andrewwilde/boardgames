$("#kickstarters").click(function(e) {

  $("#bgcontent").load('/static/html/kickstarters.html');

  $.getScript("http://code.jquery.com/jquery-migrate-1.2.1.min.js").done(function(){
    $.getScript("/static/js/slick.min.js").done(function(){
      $.getScript("/static/js/kickstarters.js");
    })
  })
});
