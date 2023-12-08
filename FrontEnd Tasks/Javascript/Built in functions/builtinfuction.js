const a=[2,4,6,8,10,12,14,16,18,20]

//Map function
function DivideBy2(a) {
    return (a/2)
}
//Reduce Function 
function RedSum(total,a) {
    return a+total
    
}

//Filter function
function FilterTest(a) {
    if (a>6) {
        return (a)
    }
}
console.log(a.map(DivideBy2))
console.log(a.filter(FilterTest))
console.log(a.reduce(RedSum))

//The Filter used above will be replicated
function Filter(a) {
    let newArray=[];
    for (let i = 0; i < a.length; i++) {
        let element = a[i];
        if (element>6) /*Replace with own condition*/ {       
            newArray.push(element)    
        }
    }
return(newArray)
}
console.log(Filter(a))

