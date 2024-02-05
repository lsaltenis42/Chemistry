function getEvenlyDividedTo(n){
    let smallestNumber = 1; 
    let found = false; 
    while (!found){
        for (let i = 1; i <= n; i++){
            if (smallestNumber % i != 0){
                smallestNumber ++
                break
            } else if(i == n){
                found = true; 
                break
            }
        }
    }

    return smallestNumber; 
}

console.log(getEvenlyDividedTo(20))