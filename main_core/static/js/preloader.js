// preloader.js

// Получаем элементы преloader'а
const preloaderWrapper = document.querySelector('.prldr');
const preloader = document.getElementById('preloader');

// Скрываем преloader при загрузке страницы
window.addEventListener('load', () => {
  preloaderWrapper.style.display = 'none';
});

// Показываем преloader при начале загрузки страницы
document.addEventListener('DOMContentLoaded', () => {
  preloaderWrapper.style.display = 'flex';
});