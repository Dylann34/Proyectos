a = prompt("Ingrese la dimensión A del Panel: ")
b = prompt("Ingrese la dimensión B del Panel: ")
x = prompt("Ingrese la dimensión X del Techo: ")
y = prompt("Ingrese la dimensión Y del Techo: ")

function calcularPaneles() {
    // Calcula cuántos paneles caben horizontalmente y verticalmente
    var panelesHorizontales = a / x
    var panelesVerticales = b / y

    // Calcula el total de rectángulos
    var totalPaneles = panelesHorizontales * panelesVerticales

    return totalPaneles
}

var totalPaneles = calcularPaneles(a, b, x, y)

console.log("La cantidad de paneles que caben dentro de las dimensiones del techo ingresadas es:" + totalPaneles)

function asignandoVar() {
    if (true) {
        var valor = 1
    }
    console.log(valor); // funciona
}

function asignandoConst () {
    if (true) {
        let valor = 1
    }
    console.log(valor); // error
}

const valor = 2 + 2

console.log(valor);