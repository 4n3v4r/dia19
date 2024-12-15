let box = document.querySelector('.box');
let input = document.querySelector('input');

input.addEventListener('input', () => {
    box.style.backgroundColor = input.value;
    box.style.borderRadius = input.value + 'px';
})
