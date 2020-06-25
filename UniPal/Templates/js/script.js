window.addEventListener("load", function() {
    setTimeout(preLoader, 1000);
});

function preLoader() {
    document.querySelector('.preloader').classList.add('hide-preloader');
}

var swiper = new Swiper('.swiper-1', {
    spaceBetween: 0,
    centeredSlides: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.pagination-1',
        clickable: true,
    },
    navigation: {
        nextEl: '.button-next-1',
        prevEl: '.button-prev-1',
    },
});
var swiper2 = new Swiper('.swiper-container-options', {
    slidesPerView: 2,
    spaceBetween: 30,
    pagination: {
        el: '.swiper-pagination-options',
        clickable: true,
    },
    autoplay: {
        delay: 5000,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        450: {
            slidesPerView: 1,
        },
        580: {
            slidesPerView: 2,
        },
        850: {
            slidesPerView: 3,
        },
    }
});