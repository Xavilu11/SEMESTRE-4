CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    color VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10,2)
);