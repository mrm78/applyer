$('[data-toggle="tooltip"]').tooltip();

// 5%*(قیمت + 1000)  
window.addEventListener("load", function() {
    setTimeout(preLoader, 1000);
});

function preLoader() {
    document.querySelector('.preloader').classList.add('hide-preloader');
}

var swiper = new Swiper('.swiper-container', {
    spaceBetween: 0,
    centeredSlides: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.main-swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.main-swiper-button-next',
        prevEl: '.main-swiper-button-prev',
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