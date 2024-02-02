function createAtom(radius){
    return {
        radius:radius,
        xPos: 0,
        yPos: 0,
        name: "",
        bonds:{},
        
    }
}

atom1 = createAtom();

console.log(atom.bonds?.firstBond);

function addOne(x){
    return x + 1;
}

let a = [];



a.push(1,2,3)

let points = [
    {x: 0, y: 1}, 
    {x: 2, y: 6}, 
    {x: 9, y: 10}, 
]

points.getDistance = function(){
    let point1 = this[0];
    let point2 = this[1];

    xDifference =  point2.x - point1.x;
    yDifference = point2.y - point1.y;

    return Math.hypot(xDifference, yDifference);
}

/** 
 *@returns Returns the number rounded to the specified number og significant figures or error message.
 *@param {number} x A numeric expresion
 *@param {number} sigfigs A numeric expresion
 */

function getRoundedToSigFigs(x, sigfigs){
    let intPart = Math.trunc(x);
    let floatPart = x - intPart;
    let lengthIntPart = x.toString().length
    if (sigfigs < 1 || typeof(x)!== 'number') {
        return 'Invalid input'
    } else if (sigfigs === 1){
        return Math.round(x);
    } else {
        let scalingFactor = 0;
        for (scalingFactor = 0; scalingFactor < sigfigs; scalingFactor++) {
            floatPart *= 10; 
        }   
        floatPart = Math.round(floatPart);  
        return (intPart * Math.pow(10,scalingFactor) + floatPart)/Math.pow(10,scalingFactor)
    }

}

//console.log(getRoundedToSigFigs(0.34567, 1));
console.log(points.getDistance())
