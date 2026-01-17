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

//Function --> Represents a block of code designed to perform a particular task
function launchTheApplication(brwoserName, URL){
    console.log("Launch the browser: "+ brwoserName);
    console.log("Navigate to the URL: "+ URL);
    console.log("Application Launched successfully..!")
}
//call the functions
launchTheApplication("Chrome","https://www.example.com");

//Date ==> date represents date and time in javascript
let currentDate = new Date();
console.log(currentDate.getFullYear());
console.log(currentDate.getMonth());

//get current year currentDate variable .getfullyear
console.log(currentDate.getFullYear());

//get current month currentDate variable .getmonth
console.log(currentDate.getMonth()+1);

//get current date currentDate variable .getdate
console.log(currentDate.getDate());

//get current hours currentDate variable .gethours
console.log(currentDate.getHours());


//get current Minutes currentDate variable .getMinutes
console.log(currentDate.getMinutes());


//get current seconds currentDate variable .getseconds
console.log(currentDate.getSeconds());

//get current milliseconds since january 1, 1970
console.log(currentDate.getMilliseconds());

/* if(month ==1){
    console.log(january);
} */

    // 5)Map===> Represents a collection of key-value pairs where keys can be of any data types.
    //
    let employeeMap = new Map();
    employeeMap.set("empid",101);
    employeeMap.set("empName","Surya");
    employeeMap.set("Having visa",true);
    employeeMap.set("empName","Reddy");
    employeeMap.delete("Having Visa");
    //Get employeee name
    console.log(employeeMap.get("empName"));
    console.log(employeeMap);
    console.log(empdetails.size)

    //6) set ==> set represents a collection of unique values of any date type

    let uniqueNumbers =new Set();
    uniqueNumbers.add(10);
     uniqueNumbers.add(20);
      uniqueNumbers.add(30);
       uniqueNumbers.add(40);
        uniqueNumbers.add(20);//duplicate value will not be added\
        uniqueNumbers.delete(30);
        console.log(uniqueNumbers.size);
        console.log(uniqueNumbers);

        //Symbol data type represents unique hidden value that you wanted to store 
        let productmanfucturing = Symbol();
        let productInfo ={
            productName: "Oneplus 9",
            productPrice: 69999,
            [productmanfucturing]: "Chennai"
        };
        console.log(productInfo);


