/* Assignment -4 (Conditional Statements & Loops)

Bank Transactions
Positive value refers Credit and Negative refers Debit Transaction
Transactions Amount
1 50000
2 -2000
3 3000
4 -15000
5 -200
6 -300
7 4000
8 -3000
First Store all the transactions in any data structure of Your Choice from collections, and by using
Loops and conditional statements
1. Print total number of credit and debit transactions completed
2. Print the total amount credited and debited in account
3. Print total amount remaining at the end in Bank Account
4. If any transaction limit exceeds +/- 10000 then print the message “Suspicious credit/ debit
Transaction with Amount” and also print total number of suspicious transactions */
        // Array of transactions: positive values represent credits, negative values represent debits
        const transactions: number[] = [50000, -2000, 3000, -15000, -200, -300, 4000, -3000];

        // Variables to store the count and amount of credits and debits
        let totalCredits: number = 0;
        let totalDebits: number = 0;
        let totalCreditAmount: number = 0;
        let totalDebitAmount: number = 0;
        let suspiciousTransactions: number = 0;

        // Iterate through each transaction in the array
        for (const amount of transactions) {

            if (amount > 0) {
                // Credit transaction
                totalCredits++;
                totalCreditAmount += amount;

                // Check for suspiciously large credit transaction
                if (amount > 10000) {
                    console.log(`Suspicious credit transaction with Amount: ${amount}`);
                    suspiciousTransactions++;
                }

            } else {
                // Debit transaction
                totalDebits++;
                totalDebitAmount -= amount; // convert to positive

                // Check for suspiciously large debit transaction
                if (amount < -10000) {
                    console.log(`Suspicious debit transaction with Amount: ${amount}`);
                    suspiciousTransactions++;
                }
            }
        }

        // Final balance
        const finalBalance: number = totalCreditAmount - totalDebitAmount;

        // Print summary
        console.log("----- Transaction Summary -----");
        console.log("Total number of credit transactions:", totalCredits);
        console.log("Total number of debit transactions:", totalDebits);
        console.log("Total amount credited:", totalCreditAmount);
        console.log("Total amount debited:", totalDebitAmount);
        console.log("Final remaining amount in the account:", finalBalance);
        console.log("Total number of suspicious transactions:", suspiciousTransactions);

        export {};