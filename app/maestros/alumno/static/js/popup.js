var btnEditUser = document.getElementById("userEdit"),
  overlay = document.getElementById("overLay"),
  popup = document.getElementById("popup"),
  iconClosePopup = document.getElementById("iconClose");

btnEditUser.addEventListener("click", function () {
  overlay.classList.add("active");
  popup.classList.add("active");
});

iconClosePopup.addEventListener("click", function () {
  overlay.classList.remove("active");
  popup.classList.remove("active");
});

var btnCreateUser = document.getElementById("createUser");
