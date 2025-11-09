const goTopBtn = document.querySelector('.go-top-btn');

window.addEventListener('scroll', () => {
  if (window.scrollY > 200) {
    goTopBtn.classList.add('show');
  } else {
    goTopBtn.classList.remove('show');
  }
});

goTopBtn.addEventListener('click', (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
