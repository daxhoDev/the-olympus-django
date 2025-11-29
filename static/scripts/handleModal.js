const planCardButtons = document.querySelectorAll(".plan-card__button");
const backdrop = document.querySelector(".backdrop");
const modalButtonNo = document.querySelector(".modal__button--no");

function openModal() {
  backdrop.classList.remove("hidden");
}

function closeModal() {
  backdrop.classList.add("hidden");
}

planCardButtons.forEach((button) =>
  button.addEventListener("click", openModal)
);
modalButtonNo.addEventListener("click", closeModal);
