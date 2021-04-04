// alert("Hola Mundo");
// var nombre = "MSQ";
// var altura = 169;
// var concatenacion = nombre +" "+ altura;
// // document.write(concatenacion);
// var datos = document.getElementById("datos");
// datos.innerHTML = concatenacion;

// if(altura >= 190){
//     datos.innerHTML += " Eres una pesona alta";
// }else{
//     datos.innerHTML += " Eres una pesona baja";
// }
 
// for(var i = 2000; i <=2020 ; i++){
//     datos.innerHTML += "estamos en el año: " + i ; 
// }

function muestraMiNombre(nombre, altura){
    // var datos = document.getElementById("datos");
    // datos.innerHTML = `
    misDatos = `
        <h1>Soy la caja de datos </h1>
        <h2>Mi nombre es: ${nombre}</h2>
        <h3>Mido ${altura} cm</h3>
        `;
    return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = muestraMiNombre("Manuel Alejandro", 169);
}

imprimir();


var nombres = ['Manu','Alejandro','Silva'];
// alert(nombres[1])

// for(var i = 0 ; i < nombres.length ; i++){
//     alert(nombres[i]);
//     // document.write(nombres[i]);
// }

nombres.forEach(function(nombre){
      document.write =(nombre + `<br/>`) ;
});