/* Create common function and then based on below details, print whether user is eligible to get the loan
or not
customerName = "John Doe";
creditScore = 720;
income = 55000.0;
isEmployed = true;
debtToIncomeRatio = 35.0; */

/* Assignment-3 (Conditional Statements)

A bank evaluates loan applicants based on the following criteria:
1. Credit Score:
o If the credit score is above 750, the loan is automatically approved.
o If the credit score is between 650 and 750, additional checks are performed.
o If the credit score is below 650, the loan is denied.
2. Income:
o For credit scores between 650 and 750, the customer’s income must be at least $50,000
for the loan to be considered.

3. Employment Status:
o If the customer’s income is at least 50,000, the system checks whether the customer is
employed.
o If the customer is unemployed, the loan is denied.
4. Debt-to-Income Ratio:
o If the customer is employed, the system checks the debt-to-income (DTI) ratio.
o If the DTI ratio is less than 40%, the loan is approved.
o If the DTI ratio is 40% or greater, the loan is denied. */
//Question 1-->A bank evaluates loan applicants based on the following criteria:--->Credit score
let custdetails={
    CustomerName: "Jhone Dee",
    CustomercreditScore: 670,
    CustomElementRegistryincome: 57000.0,
isCustomerEmployed: true,
CustomerdebtToIncomeRatio: 35.0
}

if(custdetails.CustomercreditScore>=750){
    console.log("Your credit score is above 750, the loan is automatically approved.");
}else if(custdetails.CustomercreditScore>=650 && custdetails.CustomercreditScore<=750){
console.log("your credit score is below 750 Manual review is required");}
else {
    console.log("Your credit score is not good Loan is rejected")
}

//Question 2 -->Income:
/* o For credit scores between 650 and 750, the customer’s income must be at least $50,000
for the loan to be considered. */
if(custdetails.CustomercreditScore >650 && custdetails.CustomercreditScore <=750 && custdetails.CustomElementRegistryincome >=55000){ 
    console.log("Income condition satisfied. Loan can be considered.")}
  else{
      console.log("Income should be above or equals to $55000")
  }
  /* 3. Employment Status:
o If the customer’s income is at least 50,000, the system checks whether the customer is
employed.
o If the customer is unemployed, the loan is denied. */
if (custdetails.CustomElementRegistryincome >=50000 && custdetails.isCustomerEmployed == true){
    console.log("This customer Income is satisfying and customer is salaried employee")
}
else{
    console.log("This Customer is unemployed and loan is denied")
}
 /*  3. Employment Status:
o If the customer’s income is at least 50,000, the system checks whether the customer is
employed.
o If the customer is unemployed, the loan is denied. */
if (custdetails.CustomElementRegistryincome<=49000 && custdetails.isCustomerEmployed ==false){
    console.log("This Customer is unemployed and loan is denied")
}
else{
    console.log("This customer Income is satisfying and customer is salaried employee")
}

/* 4. Debt-to-Income Ratio:
o If the customer is employed, the system checks the debt-to-income (DTI) ratio.
o If the DTI ratio is less than 40%, the loan is approved.
o If the DTI ratio is 40% or greater, the loan is denied. */ 

if (custdetails.isCustomerEmployed == true && custdetails.CustomElementRegistryincome <=40){
    console.log("This customer is employee and has the DTI Ratio")}
    else if (custdetails.CustomerdebtToIncomeRatio <= 40){
        console.log("Jhon you loan is approved");
    }
    else if (custdetails.CustomerdebtToIncomeRatio>=40){
        console.log("Jhon you DTI ration is greater than 40 and sorry your loan is denied")
    }
   






