// TESTIMONIAL
$(document).ready(function(){
    $('.testimonial-slider').slick({
      slidesToShow: 3,
      slidesToScroll: 3,
      autoplay: true,
      autoplaySpeed: 5000,
      arrows: false, // Disable arrows
      responsive: [
        {
          breakpoint: 920,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
  });