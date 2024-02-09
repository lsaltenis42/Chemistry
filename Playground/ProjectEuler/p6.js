class mathExtension{
    constructor(number){
        this.number = number; 
    }
    
    getProductAsArray(x,y){
        let product = []; 
        for(let j = 0; j <= String(x).length; j++){
    
        }
        return product
    }

    getPrimeFactorsInFactorial(x){
        if (x < 2){
            return [1];
        } else {
            let primes = []; 
            
            for(let i = 2; i <= x; i++){
                if(x % i == 0){
                    primes.push(i) 
                    x = x/i;
                }
            }
            return primes.sort((a, b) => a - b)
        }
    }

    getPowersOfPrimeFactors(){
        const primes = this.getPrimeFactorsInFactorial(this.number);
        let primesWithPowers = {};
        for (const prime of primes) {
             primesWithPowers[prime] = ((this.number - this.getSumOfDigits(this.convertToBase(this.number, prime))) / (prime - 1) );
        }
        return primesWithPowers
    }
    
    convertToBase(x, base) { 
        if (x == 0) { 
            return "0"; 
        } else { 
            return (this.convertToBase(Math.floor(x / base), base) + (x % base)); 
        } 
    } 

    getSumOfDigits(x){
        let sum = 0; 
        x = String(x);
        for(const character of x){
            sum += Number(character);
        }
        return sum;
    }
}

ExtendedMath = new mathExtension(6);

console.log(ExtendedMath.getPowersOfPrimeFactors())
