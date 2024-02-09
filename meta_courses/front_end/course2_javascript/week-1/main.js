for(let i=2;i<=9;i++){
    console.log(`\nTabuada do ${i}`);
    for(let x=1;x<=9;x++){
        console.log(`${i}x${x} = ${i*x}`);
    };
};


var i=1
if(i == 0 && i == 1) {
    console.log("Hello");
  } else {
    console.log("Goodbye");
  } 

  for (i = 0; i < 2; i++) {
    for (var j = 0; j < 3; j++) {
        console.log("Hello");
    }
}



var i = 7;
var j = 2;

if(i < 7 || j < 5) {
  console.log("Hello");
} else {
  console.log("Goodbye");
}


function letterFind(word,match){
    for(let i=0;i<word.length;i++){
        if(word[i]==match){
            console.log(`Found the ${match} at ${i}`)
        }else{
            console.log('---No match found at', i)
        }
    };
}
letterFind('test','t')

w = 'test'
console.log(w.length)


let skillsMaster = {}
skillsMaster.socialSkills = 7
skillsMaster.health = 100
skillsMaster.specialAbility = 'Space Healthy'

let skillsClasses = {
    socialSkills: 40,
    health: 80
}

console.log(skillsMaster.socialSkills,'\n',skillsClasses.socialSkills)


let obj_js = {
    'name':'Luiz',
    age:24
}
console.log(obj_js)

obj_js.name = 'Igor';
console.log(obj_js)


function arrayBuilder(a,b,c){
    arr_builder = []
    arr_builder.push(a)
    arr_builder.push(b)
    arr_builder.push(c)
    return arr_builder
}
let arr_l = arrayBuilder('att','btt','ctt')
console.log(arr_l)


function listBuilder(...args) {
    return args;
}
  
let list_builder = listBuilder('a', 'b', 'c', 'd');
console.log(list_builder);


let pi = Math.PI
let pi_round = Math.round(pi,2)

console.log(pi,pi_round)

st = 'strings'
st_arr = []
for(let i=0;i<st.length;i++){
    st_arr.push(st[i])
}


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