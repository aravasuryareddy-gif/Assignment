// variable declaration will vary based on the four different paramenters
/* initialization
reinitialisation
redeclaration
scope */


// 1. Initialization
const a = "Surya Reddy";
let b ;
let c ;
// 2. reassignment
//a="Reddy";
b=123;
c="Arava";
console.log(b);
console.log(c);
console.log(a);
//Redeclaration
/* const a= 123;
let b =21; */
var d = 1232;

//scope

{
    const x =30;
    let y = 20;
    var z = 40;
    console.log(x);
    console.log(y);
    console.log(z);
}

//console.log(x) //Error is not defined (undefined)
//console.log(y);//Error is not defined (undefined)
console.log(z);//valid
