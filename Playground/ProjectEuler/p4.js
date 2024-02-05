function getLargestPalindrome(n){
    let palindromes = [];
    let numbers = []
    for (let i = 0; i <= Number("9".repeat(n)); i++){
        for (let j = 0; j <= Number("9".repeat(n)); j++){
            let number = (i * j).toString(); 
            //console.log(`${i} * ${j}: ${number}`)
            if (isPalindrome(number) && !palindromes.includes(Number(number))) palindromes.push(Number(number))
        }
    }
    palindromes = palindromes.sort((a, b) => a - b)
    return Math.max(...palindromes);
}

function isPalindrome(number){
    if (number.length == 1) return true
    for (let k = 0; k < Math.ceil(number.length / 2); k++){
        if (number.charAt(k) != number.charAt(number.length - 1 - k))
            return false;
    }
    return true; 
}

console.log(getLargestPalindrome(3));

