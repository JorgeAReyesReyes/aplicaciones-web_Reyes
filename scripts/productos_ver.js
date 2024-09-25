document.addEventListener("DOMContentLoaded", function() {
    const ParametroURL = new URLSearchParams(window.location.search);
    const id_producto = parseInt(ParametroURL.get('id_producto'), 10);

    const productos = {
        1: {
            nombre: "FUNDA AZUL", 
            imagen: "assets/images/producto1.jpeg",
            descripcion: "Descripción del producto Funda Azul",
            precio: "$100.00"
        },
        2: {
            nombre: "FUNDA ROSA", 
            imagen: "assets/images/producto2.jpeg",
            descripcion: "Descripción del producto Funda Rosa",
            precio: "$100.00"
        },
        3: {
            nombre: "FUNDA ROJA", 
            imagen: "assets/images/producto3.jpeg",
            descripcion: "Descripción del producto Funda Roja",
            precio: "$100.00"
        },
        4: {
            nombre: "Audífonos Blancos", 
            imagen: "assets/images/producto4.avif",
            descripcion: "Descripción del producto Audífonos Blancos",
            precio: "$100.00"
        },
        5: {
            nombre: "Audífonos Morados", 
            imagen: "assets/images/producto5.webp",
            descripcion: "Descripción del producto Audífonos Morados",
            precio: "$100.00"
        }
    };

    if (productos[id_producto]) {
        document.getElementById("nombre_producto").textContent = productos[id_producto].nombre;
        document.getElementById("img_producto").src = productos[id_producto].imagen;
        document.getElementById("descripcion_producto").textContent = productos[id_producto].descripcion;
        document.getElementById("precio_producto").textContent = productos[id_producto].precio;
    } else {
        document.getElementById("nombre_producto").textContent = "Producto no disponible";
        document.getElementById("img_producto").style.display = "none";
        document.getElementById("descripcion_producto").textContent = "Descripción no disponible";
        document.getElementById("precio_producto").textContent = "Precio no disponible";
    }
});
