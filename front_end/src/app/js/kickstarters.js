$.get("http://ec2-52-14-50-132.us-east-2.compute.amazonaws.com/api/kickstarters/get_kickstarter_category?category=new", function( data ) {
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
