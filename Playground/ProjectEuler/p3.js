function getPrime(n){
    let primes = []; 
    let i = 1;

    while (n > 1 && i <= n) {
        while (n % i == 0) {
            primes.push(i);
            n = n/i;
            i ++
        }
        i ++
    }
    return primes[primes.length-1];
}

console.log(getPrime(600851475143)); 