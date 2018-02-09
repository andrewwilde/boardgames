$(function(){
  $("#menu").load('/static/html/menu.html', function() {
    $.getScript('/static/js/menu.js');
  });
});
