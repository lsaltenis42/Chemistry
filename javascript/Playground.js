let pi = 0;
let iterations = 0;

function calculatePi(n){
    n = (-1)**iterations*(2*iterations + 1);
    pi += 1/n;
    iterations ++;
    if (iterations < 10000){
        calculatePi(n);
    }
    
    return 4*pi;
}

console.log(`Calculated pi: ${calculatePi(0)} \nActual pi: ${Math.PI}`);
