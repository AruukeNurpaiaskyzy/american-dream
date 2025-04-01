const swiper = new Swiper('.courses-slider', {
    slidesPerView: 2.5,
    spaceBetween: 20,
    autoplay: {
        delay: 10000, // 10 секунд
        disableOnInteraction: false, 
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 1.2,
            spaceBetween: 10
        },
        576: {
            slidesPerView: 1.5,
            spaceBetween: 15
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        1200: {
            slidesPerView: 2.5,
            spaceBetween: 20
        }
    }
});
