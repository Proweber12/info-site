const modalWindow = document.querySelector(".modal-window");
const sliderLine = document.querySelector(".slider-line");
const prevButton = document.querySelector(".prev-button");
const nextButton = document.querySelector(".next-button");
const slides = document.querySelectorAll(".slider-line img");
const photos = document.querySelectorAll(".album__item");
const img = document.querySelectorAll(".album__item");
console.log(img);

let position = 0;

photos.forEach((item, index) => {
  item.addEventListener("click", function () {
    modalWindow.style.display = "block";
    document.body.style.overflow = "hidden";
  });
});

modalWindow.addEventListener("click", function (event) {
  let button = event.target.closest("button");
  let img = event.target.closest("img");
  if (button) return;
  else if (img) return;
  modalWindow.style.display = "none";
  document.body.style.overflow = "";
});

const nextSlide = () => {
  if (position < (slides.length - 1) * sliderLine.clientWidth) {
    position += sliderLine.clientWidth;
  } else {
    position = 0;
  }

  sliderLine.style.left = -position + "px";
};

nextButton.addEventListener("click", nextSlide);

const prevSlide = () => {
  if (position > 0) {
    position -= sliderLine.clientWidth;
  } else {
    position = (slides.length - 1) * sliderLine.clientWidth;
  }
  sliderLine.style.left = -position + "px";
};

prevButton.addEventListener("click", prevSlide);

photos.forEach((item, index) => {
  item.addEventListener("click", () => {
    position = sliderLine.clientWidth * index;
    sliderLine.style.left = -position + "px";
  });
});
