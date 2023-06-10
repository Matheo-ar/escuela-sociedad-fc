var btnAbrirPopUp = document.getElementById("btn-logout-home"),
  overlay = document.getElementById("overlay"),
  popup = document.getElementById("pop-up"),
  btnCerrarPopup = document.getElementById("btn-cerrar-popup"),
  btnNo = document.getElementById("btn-no")

btnAbrirPopUp.addEventListener("click", function() {
  overlay.classList.add("active");
  popup.classList.add("active");
})

btnCerrarPopup.addEventListener("click", function() {
  overlay.classList.remove("active");
  popup.classList.remove("active");
})

btnNo.addEventListener("click", function() {
  overlay.classList.remove("active");
  popup.classList.remove("active");
})
