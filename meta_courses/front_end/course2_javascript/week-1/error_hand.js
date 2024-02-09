let addTwoNumbs = (a,b)=>{
    try{
        if(typeof(a!='number')){
            throw new ReferenceError('the first argument is not a number');
        }else if(typeof(b!='number')){
            throw new ReferenceError('the second argument is not a number');
        }else{
            console.log(a+b);
        }
    }catch(err){
        console.log("Error!", err)
    }
    console.log('It still works')
}

addTwoNumbs(5,"5")



function letterFinder(word, match) {
    let condition_word = typeof(word)=='string' && word.length>=2;
    let condition_match = typeof(match)=='string' && match.length==1;

    if(condition_word && condition_match){
        for(var i = 0; i < word.length; i++) {
            if(word[i] == match) {
                //if the current character at position i in the word is equal to the match
                console.log('Found the', match, 'at', i)
            } else {
                console.log('---No match found at', i)
            }
        }
    }else{
        console.log("Please pass correct arguments to the function.")
    }
}
let let_find = letterFinder(123,'c')




var result = null;
console.log(result);


try {
    console.log('Hello');
  } catch(err) {
    console.log('Goodbye');
  }


var x;

if(x === null) {
console.log("null");
} else if(x === undefined) {
console.log("undefined");
} else {
console.log("ok");
}


try {
    Number(5).toPrecision(300)
    } catch(e) {
    console.log("There was an error")
    }