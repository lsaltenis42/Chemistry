let sum = 0; 

function getSumOfEvenFibonacci(n){
    let a_nMinus2 = 0, a_nMinus1 = 1; 
    a_n = a_nMinus2 + a_nMinus1

    while (a_n < n){
        if (a_n % 2 == 0){
            sum += a_n;
        }   
        a_n = a_nMinus2 + a_nMinus1;  
        a_nMinus2 = a_nMinus1;
        a_nMinus1 = a_n; 
    }

    return sum; 
}

console.log(getSumOfEvenFibonacci(4_000_000));
