const deleteUserButtons = document.querySelectorAll(".button--delete-user");
const backdrop = document.querySelector(".backdrop");
const modalButtonNo = document.querySelector(".modal__button--no");
const deleteUserForm = document.getElementById("deleteUserForm");

let currentUserId = null;

function openModal(userId) {
  currentUserId = userId;
  deleteUserForm.action = `/user/delete/${userId}/`;
  backdrop.classList.remove("hidden");
}

function closeModal() {
  backdrop.classList.add("hidden");
  currentUserId = null;
}

deleteUserButtons.forEach(button => {
  button.addEventListener("click", () => {
    const userId = button.getAttribute("data-user-id");
    openModal(userId);
  });
});

modalButtonNo.addEventListener("click", closeModal);

// Cerrar modal al hacer clic en el backdrop
backdrop.addEventListener("click", (e) => {
  if (e.target === backdrop) {
    closeModal();
  }
});
