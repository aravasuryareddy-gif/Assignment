// loop statements:-- statements or repeat the execution of statements multiple times based on the condition

//For loop
//while loop
//For loop will be sused when we we know the total number of iteraion to be executed//
//while loop when we dontnt kknow the the number of iterations needds to be dexecuted

// for loop 
//syntax: where to begin where to stop
//for(condition-to-Start; condtion to end; increament/decreament)
{
    //statements
}

//example:== prin the name Surya for 10 times using for loop
let name:string ="Surya Reddy"
for (let name :number =1; name <=10; name++)
{
    console.log(name + "Surya Reddy")
}

//while loop:-- 
//syntax
//while (condition)
{
    //statements

}


// Example:-- Refresh the page until the application is launched successfully
let counter:number =1;
while(counter>0){
    let isPageLoaded:boolean =false; // assume this value is coming from application
    if(isPageLoaded || counter ===10){
        break; // determine the loop when the page is loaded or not loaded even after 10
    }



}
    console.log("Refresh the page");
