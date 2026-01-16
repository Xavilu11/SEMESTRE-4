const form = document.getElementById("registroForm");
const submitBtn = document.getElementById("submitBtn");

const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const edad = document.getElementById("edad");

const errorNombre = document.getElementById("errorNombre");
const errorEmail = document.getElementById("errorEmail");
const errorPassword = document.getElementById("errorPassword");
const errorConfirm = document.getElementById("errorConfirm");
const errorEdad = document.getElementById("errorEdad");

function validarFormulario() {
  let valido = true;

  // Nombre
  if (nombre.value.length < 3) {
    errorNombre.style.display = "block";
    valido = false;
  } else errorNombre.style.display = "none";

  // Email
  const regexEmail = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
  if (!regexEmail.test(email.value)) {
    errorEmail.style.display = "block";
    valido = false;
  } else errorEmail.style.display = "none";

  // Password
  const regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$/;
  if (!regexPassword.test(password.value)) {
    errorPassword.style.display = "block";
    valido = false;
  } else errorPassword.style.display = "none";

  // Confirmación
  if (confirmPassword.value !== password.value || confirmPassword.value === "") {
    errorConfirm.style.display = "block";
    valido = false;
  } else errorConfirm.style.display = "none";

  // Edad
  if (parseInt(edad.value) < 18 || edad.value === "") {
    errorEdad.style.display = "block";
    valido = false;
  } else errorEdad.style.display = "none";

  // Habilitar botón
  submitBtn.disabled = !valido;
}

// Validaciones en tiempo real
[nombre, email, password, confirmPassword, edad].forEach(campo => {
  campo.addEventListener("input", validarFormulario);
});

// Envío del formulario
form.addEventListener("submit", function(event) {
  event.preventDefault();
  alert("Formulario enviado correctamente ✅");
});