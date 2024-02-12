//example of adding properties and methods to an object
var car = {};
car.mileage = 98765;
car.color = "red";
console.log(car);
car.turnTheKey = ()=> {
    console.log("The engine is running")
}
car.lightsOn = ()=> {
    console.log("The lights are on.")
}
console.log(car);
car.turnTheKey();
car.lightsOn()

let sumN = (a,b)=>{
    return a/b
}

console.log(sumN(0,5))