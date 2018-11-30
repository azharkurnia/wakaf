$(document).ready(function(){
  $(".owl-carousel").owlCarousel();
});

$('.owl-carousel').owlCarousel({
    autoplay:true,
    loop:true,
    center:true,
    nav:true,
    autoWidth:true,
    navText : ['<i class="fa fa-arrow-left" aria-hidden="true"></i>','<i class="fa fa-arrow-right" aria-hidden="true"></i>'],
    responsive:{
        0:{
            items:1
        },
        480:{
            items:2
        },
        720:{
            items:3
        },
    }
})
