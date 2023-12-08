// function Pure() {
//     for (let i = 0; i < 10; i++) {
//         console.log(`pure function is running ${i+1}`)
//     }
    
// }

// //Impure function
// function Impure() {
//     for (let i = 0; i < 10; i++) {
//         console.log("impure function is running",Math.floor(Math.random() * 100));
//     }
// }
// Pure()
// Impure()

//Higher order functions
function Outermost() {
    console.log("the outermost is run")
    
}
function Outer(a) {
    console.log("outer function has been called")
    a()
    return function Inner() {
        console.log("Inner function has been returned")
    }
    
}
let funct=Outer(Outermost)
funct()