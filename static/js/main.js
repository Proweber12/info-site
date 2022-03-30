const mainGreenButtons = document.querySelectorAll(".main__news-button span");
const hideBlocksNews = document.querySelectorAll(".main__post-hide");
const hideBlockBuild = document.querySelectorAll(".main__hide-posts");
const post = document.querySelector(".main__post");
const mainMenuList = document.querySelectorAll(".sidebar__list");
const sliderLine = document.querySelector(".slider-line");
const prevButton = document.querySelector(".prev-button");
const nextButton = document.querySelector(".next-button");
const sliders = document.querySelectorAll(".slider-line img");
console.log(sliders);
let position = 0;
mainGreenButtons.forEach((item, index) => {
  item.addEventListener("click", function (event) {
    const buttons = Array.from(mainGreenButtons);
    if (event.target == buttons[0]) {
      hideBlocksNews.forEach((item) => {
        item.style.height = post.offsetHeight + "px";
        item.style.opacity = 1;
        item.style.zIndex = 1;
      });
    } else {
      hideBlockBuild.forEach((item) => {
        item.style.height = post.offsetHeight + "px";
        item.style.opacity = 1;
        item.style.zIndex = 1;
      });
    }
  });
});

const nextSlide = () => {
  if (position < (sliders.length - 1) * sliderLine.clientWidth) {
    position += sliderLine.clientWidth;
  } else {
    position = 0;
  }

  sliderLine.style.left = -position + "px";
};

const prevSlide = () => {
  if (position > 0) {
    position -= sliderLine.clientWidth;
  } else {
    position = (sliders.length - 1) * sliderLine.clientWidth;
  }

  sliderLine.style.left = -position + "px";
};
nextSlide();
nextButton.addEventListener("click", nextSlide);
prevButton.addEventListener("click", prevSlide);
