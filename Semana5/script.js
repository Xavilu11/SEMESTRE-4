const gallery = document.getElementById("gallery");
const addImageUrlBtn = document.getElementById("addImageUrlBtn");
const addImageFileBtn = document.getElementById("addImageFileBtn");
const deleteImageBtn = document.getElementById("deleteImageBtn");
const imageUrlInput = document.getElementById("imageUrl");
const imageFileInput = document.getElementById("imageFile");

let selectedImage = null;

// Función para manejar selección única
function selectImage(img) {
  if (selectedImage) selectedImage.classList.remove("selected");
  img.classList.add("selected");
  selectedImage = img;
}

// Crear y configurar un <img>
function createGalleryImage(src) {
  const img = document.createElement("img");
  img.src = src;
  img.addEventListener("click", () => selectImage(img));
  return img;
}

// Agregar imagen desde URL
addImageUrlBtn.addEventListener("click", () => {
  const url = imageUrlInput.value.trim();
  if (!url) return;
  const img = createGalleryImage(url);
  gallery.appendChild(img);
  imageUrlInput.value = "";
});

// Agregar imagen desde archivo local
addImageFileBtn.addEventListener("click", () => {
  const file = imageFileInput.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (e) => {
    const img = createGalleryImage(e.target.result);
    gallery.appendChild(img);
    imageFileInput.value = "";
  };
  reader.readAsDataURL(file);
});

// Eliminar imagen seleccionada
deleteImageBtn.addEventListener("click", () => {
  if (!selectedImage) return;
  gallery.removeChild(selectedImage);
  selectedImage = null;
});

// Atajos de teclado
document.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && imageUrlInput === document.activeElement) {
    addImageUrlBtn.click();
  }
  if (event.key === "Delete" && selectedImage) {
    deleteImageBtn.click();
  }
});