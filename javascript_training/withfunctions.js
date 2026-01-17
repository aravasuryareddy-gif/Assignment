// TEST CASE 1:-- validating the home page
loginIntoApplication()
/* Launch the chrome browser,
Enter URL "www.icici.com" and Launch the application.
Enter username as "Surya",
enter password as "surya@16".
click on the login button 
Verify that the homw page is displayed with welcome message
close the browser*/
logoutAndCloseBrowser()



//test case 2 validating  the fund transfer page
loginIntoApplication()
/* 
navigate to the fund transfer pafe
enter the beneficiary account number as '1242332'
enter amount to transfer as "5000"
click on the transfer button
verify that the fund transfer is successfull with the message "transfer successfull"
logout from the application
close the browswer*/
logoutAndCloseBrowser()


//Test case 3 :-- validating the account statemnt page
loginIntoApplication()
/*
navigate to the account statement page
select the date range from "01-jan-2023" to "31-jan-2023"
click on the generate statement button
verify that the account stattemnet is displayed for the slected date range
log out form the application
close the browser*/
logoutAndCloseBrowser()

//==========================================================================================================
function loginIntoApplication(browserName, URL, username){//function with parameter --> adding placeholder to accept dynamic value of browsername

//Launch the +brwoserName browser,
//Enter URL +URL and Launch the application.
//Enter username as +username,
//enter password as "surya@16".
//click on the login button 
}
function logoutAndCloseBrowser(){
    //Logout from the application.
    //close the browser
}

//how to create functions in javascript or typescript?
//1. Identify the duplicate code and seperate the same from actual test script
//2. create a block and copy those duplicate steps inside the block.
//3. Give a valid and meaning full name to that particular block to call the function easily whenever is required.
