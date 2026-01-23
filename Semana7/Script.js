// Arreglo inicial de prendas textiles
const prendas = [
  { nombre: "Camiseta básica", precio: 10, descripcion: "Algodón 100%, disponible en varios colores." },
  { nombre: "Jeans clásicos", precio: 35, descripcion: "Ajuste perfecto, hecho con calidad." },
  { nombre: "Abrigo ligero", precio: 40, descripcion: "Ideal para todo compromiso, material impermeable." },
  { nombre: "Vestido casual", precio: 35, descripcion: "Fresco y cómodo, perfecto para verano." }
];

// Función para renderizar la lista
function renderizarPrendas() {
  const lista = document.getElementById("product-list");
  lista.innerHTML = ""; // Limpiar antes de renderizar

  prendas.forEach(prenda => {
    const item = document.createElement("li");
    // Formatear precio con dos decimales
    item.textContent = `${prenda.nombre} - $${prenda.precio.toFixed(2)} | ${prenda.descripcion}`;
    lista.appendChild(item);
  });
}

// Renderizar automáticamente al cargar la página
window.onload = renderizarPrendas;

// Evento para agregar una nueva prenda desde el formulario
document.getElementById("add-product").addEventListener("click", () => {
  const nombre = document.getElementById("nombre").value.trim();
  const precio = parseFloat(document.getElementById("precio").value);
  const descripcion = document.getElementById("descripcion").value.trim();

  if (nombre && !isNaN(precio) && descripcion) {
    const nuevaPrenda = { nombre, precio, descripcion };
    prendas.push(nuevaPrenda);
    renderizarPrendas();

    // Limpiar campos después de agregar
    document.getElementById("nombre").value = "";
    document.getElementById("precio").value = "";
    document.getElementById("descripcion").value = "";
  } else {
    alert("Por favor completa todos los campos correctamente.");
  }
});