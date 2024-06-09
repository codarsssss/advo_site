var swiper = new Swiper(".mySlider", {
  slidesPerView: 3,
  spaceBetween: 60,
  loop: true,
  autoplay: {
    delay: 5000,
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    720: {
      slidesPerView: 2,
      spaceBetween: 40
    },
    1000: {
      slidesPerView: 3,
      spaceBetween: 60
    }
  }
});