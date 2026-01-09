//Primitive data types
/* 
Data types are two different categories
primitive data types and non-primitive data types

*/

// Primitive Data type
 

//number --> Represents numbers with decimals and without decimals( without quotes )
let num = 123;
let floatnum = 1.232;
let string = 'surya';
console.log(typeof num);
console.log(typeof floatnum);
console.log(typeof string);
//String --> Represents sequence of characters wrapped inside signle or double quotes
let str ="Surya ";
let str1 ="Reddy";
let str2 ='Arava';
console.log(typeof str);
console.log(typeof str1);
console.log(typeof str2);
//Boolean -> Represents results of condition : true or false

let isstudent = true;
let isskyisgreen =false;
console.log(typeof isstudent);
console.log(typeof isskyisgreen);
// Undefined --> undefined represents a varaible that has been declared but not assigned a value.

let undefvar ;
console.log(typeof undefvar);

// Null --> Represnts an intentional absence of any object value
let nullval =null;
console.log(typeof nullval);

//Synmbol --> Represents a unique identifier
let sym = Symbol
console.log(typeof sym);

//==============================================================================

//      Non -Primitive data types

/// =============================================================================

//Object --> represnts a collection of key-values pairs.

let empdetails ={

empID : 101,
empname : "surya reddy",
havingvisa: true,
address:{
    city: 'New york',
    zip_code: 1234,
    state : 'NY',
    country: "USA"

}
};
console.log(empdetails.empID);
console.log(empdetails.empname);
console.log(empdetails.address);
console.log(empdetails.havingvisa);
console.log(empdetails.address.city);
console.log(empdetails.address.country);
console.log(empdetails.address.state);
console.log(empdetails.address.zip_code);
console.log(empdetails);

// Array --> Represents the ordered collection of items
let fruits = ["apple", "Banana","grapes","orange"];
let fruitsandprices =["apple", 120 ,"Banana", 200, "grapes", 50, "orange", 100];
let fruitpricesandavailablity =["apple", 120 ,true, "Banana", 200,false, "grapes", 50, true,"orange", 100,false];
//console.log(fruits);
// Print banana from fruits array 
console.log(fruits[1]);
// print grapes price from the fuitsandprices array
console.log(fruitsandprices[5]);
// print availability of the fruit 
console.log(fruitpricesandavailablity[5]);