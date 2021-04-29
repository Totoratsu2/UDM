function promedio() {
    const resultado = document.getElementById('resultado');
    const numero = document.getElementById('numero');

    let numeros = []

    numeros.push(parseFloat(numero.innerHTML));
    numero.innerHTML = '';

    let suma = 0;
    for(let i =0; i<numeros.length; i++){
        suma = suma + numeros[0];
    }

    resultado.innerHTML = `Resultado: ${suma}`;
}