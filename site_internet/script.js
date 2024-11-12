// script.js
function addToCart(productId) {
    var quantityElement = document.getElementById("quantity-" + productId);
    var quantity = parseInt(quantityElement.innerText);

    if (quantity > 0) {
        quantity--;
        quantityElement.innerText = quantity;

        if (quantity <= 10) {
            alert("Il reste moins de 5 articles pour cet article !");
        }

        addToCartBackend(productId);
    } else {
        alert("Cet article est en rupture de stock !");
    }
}

function addToCartBackend(productId) {
    // Fonction backend pour ajouter au panier (à implémenter)
}
