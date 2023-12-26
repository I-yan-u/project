$(document).ready(() => {

  // nav dropdown
  $('.header #show').click(() => {
    $('.header').animate({'height': '180px'}, 1000);
    $('.header .nav').animate({opacity: '1'}, 1000);
    $('.header #show').css({ display: 'none' }).fadeOut('fast');
    $('.header #close').css({ display: 'block' }).fadeIn('slow');
    $('.header .nav').css({ display: 'flex' }).slideDown('slow');
  });

  $('.header #close').click(() => {
    $('.header #close').css({ display: 'none' }).fadeOut('fast');
    $('.header #show').css({display: 'block'}).fadeIn('slow');
    $('.header .nav').animate({opacity: '0'}, 1000);
    // $('.header .nav').css({ display: 'none' }).slideUp('slow');
    $('.header').animate({'height': '50px'}, 1000);
  });
});