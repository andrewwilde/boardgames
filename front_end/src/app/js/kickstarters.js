$.get("/api/kickstarters/get_limited_kickstarters", function( data ) {
  html = "";
  $.each(data, function(index, value) {
    $('.autoplay').append('<div><iframe src="' + value + '" width="200px" height="500px" frameborder="0"></iframe></div>\n');
  });

  $('.autoplay').slick({
    lazyLoading: 'progressive',
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
  });
});
