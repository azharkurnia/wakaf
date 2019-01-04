$(document).ready(function(){
    $(".owl1").owlCarousel();
    $(".owl2").owlCarousel();

});

$('.owl1').owlCarousel({
    autoplay:true,
    loop:true,
    nav:true,
    autoWidth:true,
    autoHeight:true,
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
        }
    }
});

$('.owl2').owlCarousel({
    center:true,
    margin:0,
    loop:true,
    nav:true,
    autoHeight:true,
    items:2,
    navText : ['<i class="fa fa-arrow-left" aria-hidden="true"></i>','<i class="fa fa-arrow-right" aria-hidden="true"></i>']
});
