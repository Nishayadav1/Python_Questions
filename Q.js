// question-1if we have given three  numbers 10 and 100,20 then output should be 100 as it is greater in those three numbers.

// function maxNumber(a,b,c){
//   var n= Math.max(a,b,c);
//   return n
// }
// let x=parseInt(prompt())
// let y=parseInt(prompt())
// let z=parseInt(prompt())
// console.log("max Number=",maxNumber(x,y,z))


// question2-if user given two sides as one side is 40 and another side is 40. then output should be "Square"
// if user given two sides as one side 40 and another is 20 then output should be "Rectangle".

// function shapes(a,b){
//     if (a==b){
//         console.log("squre")
//     }else{
//         console.log("rectangle")
//     }
// }
// x=parseInt(prompt())
// y=parseInt(prompt())
// shapes(x,y)

// question3
// function profitAndLoss(sp,cp){
//     if (sp>cp){
//         let profit=sp-cp;
//         console.log("profit=",profit);
//     }else if(cp>sp){
//         let loss=cp-sp;
//         console.log("loss=",loss)
//     }else{
//         console.log("no profit,no loss")
//     }
// }
// x=parseInt(prompt())
// y=parseInt(prompt())
// profitAndLoss(x,y)

// question-4
// Write a program to check whether a number is the smallest 4 digit number.
//  function smallest(a){
//      if (a<4){
//          console.log("its smallest")
//      }else{
//          console.log("its not a smallest")
//      }
//  }
// smallest(parseInt(prompt()))


// questions-5
// Write a program to check whether a number is the largest 3 digit number.
//  function largest(a){
//      if (a>3){
//          console.log("its largest")
//      }else{
//          console.log("its not a largest")
//      }
//  }
// largest(parseInt(prompt()))

// questions-6
// Write a program to check whether a number is divisible by 7 or not.
// function divisible(a){
//     if (a%7==0){
//     console.log("yes its divisible")
//     } else{
//         console.log(" its not divisible")
//     }
// }
// divisible(parseInt(prompt()))


// quetion-7-Write a program to check whether a number is even or odd.
// function oddAndEven(a){
//     if (a%2==0){
//     console.log("yes its Even")
//     } else{
//         console.log(" its  odd")
//     }
// }
// oddAndEven(parseInt(prompt()))


// question-8-Write a program to check whether the last digit of a number (entered by user) is divisible by 3 or not.
// function num(n){
//     let a=n%10
//     if (a%3==0){
//         console.log("yes its divisible by 3")
//     }else{
//         console.log("its not divisible by 3")
//     }
// }
// num(parseInt(prompt()))

// question-9-Write a program to check whether a person is eligible for voting or not. Age for voting is 18 years.
// function voting(age){
//     if(age>17){
//         console.log("its eligible")
//     }else{
//         console.log("its not eligible")
//     }
// }
// voting(parseInt(prompt()))


// question-10-
// Write a program to display "Hello" if a number entered by the user is a multiple of five , otherwise print "Bye".
// function num(n){
//     if(n%5==0){
//         console.log("hello")
//     }else{
//         console.log("bye")
//     }
// }
// num(parseInt(prompt()))

// question-11-Write a program to check whether a number entered is a three digit number or not.
// function digit(n){
//     let c=0;
//     let num=n
//     while (num>0){
//         let a=num %10;
//         c++;
//         num=Math.floor(num/10);
//     }if (c==3){
//         console.log("its three digit number")
//     }else{
//         console.log("its not a three digit number")
//     }
// }
// digit(parseInt(prompt()))


// question-12-Write a program to check whether a person is a senior citizen or not(Senior citizen Age=60).
// function voting(age){
//     if(age>=60){
//         console.log("its senior citizen")
//     }else{
//         console.log("its not a senior citizen")
//     }
// }
// voting(parseInt(prompt()))


// question-13-Accept the temperature in degrees Celsius of water and check whether it is boiling temperature or not (boiling point of water is 100 C)
// function boil(x){
//     if (x==100){
//         console.log("its boiling")
//     }else{
//         console.log("its not boiling")
//     }
// }
// boil(parseInt(prompt()))


// question-14-A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for the user.
// function dis(q){
//     if(q>1000){
//         let a=100*q;
//         let b=(a*10)/100;
//         return b;
//     }else{
//         return a;
//     }
// }
// console.log(dis(1234))

// question-15-A company decided to give a bonus of 5% of his salary to an employee if his/her year of service is more than 5 years. Ask users for their salary and year of service and print the bonus amount.
// function bonus(salary,year){
//     if(year>5){
//         let a=(salary*5)/100
//         let ts=salary+a
//         return ts
//     }else{
//         return salary
//     }
    
// }
// console.log(bonus(parseInt(prompt()),parseInt(prompt())))


// question-16-A student will not be allowed to sit in an exam if his/her attendance is less than 75%. Take following input from the user. Number of classes held. Number of classes attended. And print, percentage of class attended. Is the student allowed to sit in the exam or not.

// question-17-Take an integer N as input and check whether it ends with 3 or 7. If it ends with 3, print “ends with 3”, if it ends with 7, print “ends with 7”, otherwise print the number itself.


// question-18-Write a program to take two numbers as input and print their difference if the first number is greater than the second number, otherwise print their sum.


// question-19-Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4, otherwise, decrement its value by 1.


// question-20-Write a program to obtain 2 numbers (A and B) and an arithmetic operator (C) and then design a calculator depending upon the operator entered by the user.

// question-21-Write a program to input the length (L) and breadth (B) of a rectangle and output whether its area is greater or perimeter is greater or both are equal.


// question-22-Write a program to input the month number and print the number of days in that month. Take an input from the user between 1 and 12 inclusive. (Output 28 days for the month of February)



// question-23-Write a program to input a number and output whether a number is negative, positive or zero.


// question-24- 
 	

// 47 of 200 rows displayed
// Input any city from the user and display the monument of that city.
//                   City                                 Monument
//                   Delhi                               Red Fort
//                   Agra                                Taj Mahal
//                   Jaipur                              Jal Mahal
// For any other city as an input, print "No monument in the database for this city.".



// question-25- 
// Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer out of 100. Calculate percentage and grade according to following:
// Percentage >= 90% : Grade A
// Percentage >= 80% : Grade B
// Percentage >= 70% : Grade C
// Percentage >= 60% : Grade D
// Percentage >= 40% : Grade E
// Percentage <   40% : Grade F


// question-26-Write a program to input basic salary of an employee and calculate its Gross salary according to following: (Gross salary is the sum of basic salary, HRA, and DRA)
// Basic Salary <= 10000 : HRA = 20%, DA = 80%
// Basic Salary <= 20000 : HRA = 25%, DA = 90%
// Basic Salary > 20000 : HRA = 30%, DA = 95%

// question-27- 
// Roller Coasters require children to have a minimum height of 5 feet. Any child below this height is generally not allowed on them. Write a program to accept a child’s height in inches and display if he or she will be allowed to ride or not.

// question-28- 
// Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
//         Cost price (in Rs)                                               Tax
//         > 100000                                                            15 %
//         > 50000 and <= 100000                                   10%
//         <= 50000                                                             5%

// question-29-Write a program to find a maximum between three numbers. (Use minimum number of comparisons without using logical operators - and, or)



// question-30- 
// Input a date in with day, month and year in different lines and output if it is valid. If its valid, print valid, else print invalid.
// (Hint: The year in the date must be greater than zero, the months must lie between 1 and 12, and the days must lie between 1 and 31, depending on the month number. If the year is a leap year February will have 29 days as opposed to 28 in non leap years)



// question-31- 
// Write a program to input electricity unit charges and calculate the total electricity bill according to the given condition:
// For the first 50 units Rs. 0.50/unit
// For next 100 units Rs. 0.75/unit
// For the next 100 units Rs. 1.20/unit
// For unit above 250 Rs. 1.50/unit
// An additional surcharge of 20% is added to the bill



// question-32- 
// Write a program to calculate the electricity bill (Accept the number of units from the user) according to the following criteria:                                                                           Unit                                                 Price  
// First 100 units                                                       no charge
// Next 100 units                                                      Rs 5 per unit
// After 200 units                                                     Rs 10 per unit

// question-33- 
// Accept the age, gender (‘M’,   ‘F’), and the number of days and display the wages accordingly
// If the age does not fall in any range then display the following message: “Enter appropriate age”
//                 Age:                            Gender                        Wage/day
//       >=18 and <30                          M                              700    
//                                                           F                               750
//       >=30 and <=40                        M                              800
//                                                           F                               850 


// question-34- 
// Accept the number of days from the user and calculate the charge for the library according to the following:
// First five days:                 Rs 2/day.
// Next 5 days:                    Rs 3/day.
// Next 5  days:                   Rs 4/day
// After 15 days:                 Rs 5/day



// question-35- Input four sides of a quadrilateral ABCD in the order AB, BC, CD, DA and an internal angle I and write a program to categorize the shape of a quadrilateral as either a square, rhombus, rectangle, parallelogram, or irregular quadrilateral.

// question-36- Write a program to input two numbers and sum them. However, if the sum is between 15 to 20 it will return 20.

















