//2 switch case statement--> when we know the result of condition before execution.
let env:string ="prod";

switch(env)
{
    case "dev":
    console.log("login into the application with 'dev.netflix.com'");
    break;
     case "QA":
    console.log("login into the application with 'qa.netflix.com'");
    break;
     case "UAT":
    console.log("login into the application with 'uat.netflix.com'");
    break;
     case "prod":
    console.log("login into the application with 'www.netflix.com'");
    break;
}
