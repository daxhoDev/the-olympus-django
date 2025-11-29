const planCardButtons = document.querySelectorAll('.plan-card__button');
const backdrop = document.querySelector('.backdrop')
const modalButtons = document.querySelectorAll('.modal__button');

function openModal() {
    backdrop.classList.remove('hidden')
}

function closeModal() {
    backdrop.classList.add('hidden')
}

planCardButtons.forEach(button => button.addEventListener('click', openModal))
modalButtons.forEach(button => button.addEventListener('click', closeModal))