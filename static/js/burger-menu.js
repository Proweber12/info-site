const burgerMenu = document.querySelector(".burger-button");
const aside = document.querySelector("aside");
const closeIcon = document.querySelector(".close-icon");

burgerMenu.addEventListener("click", function () {
  aside.style.left = 0 + "vw";
  document.body.style.overflow = "hidden";
});

closeIcon.addEventListener("click", function () {
  aside.style.left = "";
  document.body.style.overflow = "";
});
