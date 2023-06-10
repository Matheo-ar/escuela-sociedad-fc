// overlay actualizar categorias
var btnEditCategories = document.getElementById("categoriesEdit"),
  overlayCategories = document.getElementById("overLayCategories"),
  popupCategories = document.getElementById("popupCategories"),
  iconClosePopupCategories = document.getElementById("iconCloseCategories");

btnEditCategories.addEventListener("click", function () {
  overlayCategories.classList.add("active");
  popupCategories.classList.add("active");
});

iconClosePopupCategories.addEventListener("click", function () {
  overlayCategories.classList.remove("active");
  popupCategories.classList.remove("active");
});

// overlay crear categorias
var btnCreateCategories = document.getElementById("buttonCreateCategories"),
  overlayCreateCategories = document.getElementById("overLayCreateCategories"),
  popupCreateCategories = document.getElementById("popupCreateCategories"),
  iconCloseCreateCategories = document.getElementById(
    "iconCloseCreateCategories"
  );

btnCreateCategories.addEventListener("click", function () {
  overlayCreateCategories.classList.add("active");
  popupCreateCategories.classList.add("active");
});

iconClosePopupCreateCategories.addEventListener("click", function () {
  overlayCreateCategories.classList.remove("active");
  popupCreateCategories.classList.remove("active");
});

var btnCreateCategories = document.getElementById("buttonCreateCategories");
