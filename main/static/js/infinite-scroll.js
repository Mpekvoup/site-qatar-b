document.addEventListener("DOMContentLoaded", function () {
  const scrollContainers = document.querySelectorAll(".logos-scroll");

  scrollContainers.forEach((container) => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) {
            const cards = container.children;
            const firstCard = cards[0];
            const lastCard = cards[cards.length - 1];

            if (entry.target === firstCard) {
              container.appendChild(firstCard.cloneNode(true));
              container.style.transform = "translateX(0)";
            } else if (entry.target === lastCard) {
              container.prepend(lastCard.cloneNode(true));
            }
          }
        });
      },
      {
        threshold: 0,
      }
    );

    // Наблюдаем за первым и последним элементами
    const cards = container.children;
    observer.observe(cards[0]);
    observer.observe(cards[cards.length - 1]);
  });
});
