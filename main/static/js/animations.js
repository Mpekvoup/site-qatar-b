document.addEventListener("DOMContentLoaded", function () {
  const burgerMenu = document.querySelector(".burger-menu");
  const nav = document.querySelector(".nav");
  const menuOverlay = document.querySelector(".menu-overlay");

  // Проверяем наличие элементов перед добавлением обработчиков
  if (!burgerMenu || !nav || !menuOverlay) {
    console.error("One or more menu elements not found");
    return;
  }

  burgerMenu.addEventListener("click", function (e) {
    e.preventDefault(); // Предотвращаем стандартное поведение
    burgerMenu.classList.toggle("active");
    nav.classList.toggle("active");
    menuOverlay.classList.toggle("active");
    document.body.style.overflow = nav.classList.contains("active")
      ? "hidden"
      : "";
  });

  menuOverlay.addEventListener("click", function () {
    burgerMenu.classList.remove("active");
    nav.classList.remove("active");
    menuOverlay.classList.remove("active");
    document.body.style.overflow = "";
  });

  // Закрытие меню при клике на ссылку
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", function () {
      burgerMenu.classList.remove("active");
      nav.classList.remove("active");
      menuOverlay.classList.remove("active");
      document.body.style.overflow = "";
    });
  });
});
