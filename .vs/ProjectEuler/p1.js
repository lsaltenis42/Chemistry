function getSumOfMultiples(x){
    let sum = 0;
    
    if (x < 3) return 0; 

    for (let num = 1; num < x; num++){
        if (num % 3 == 0 || num % 5 == 0){
            sum += num;
        }     
    }

    return sum;
}

console.log(getSumOfMultiples(1000))