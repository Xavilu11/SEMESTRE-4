// Botón de alerta
document.getElementById("alertBtn").addEventListener("click", function() {
  alert("¡Bienvenido a Harta Pinta! 🌿 Descubre nuestros productos únicos.");
});

// Validación del formulario
document.getElementById("contactForm").addEventListener("submit", function(event) {
  event.preventDefault();
  let form = event.target;
  if (!form.checkValidity()) {
    event.stopPropagation();
  } else {
    alert("Formulario enviado correctamente ✅");
    form.reset();
  }
  form.classList.add("was-validated");
});