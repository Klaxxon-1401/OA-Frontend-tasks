// const doc=document
// console.log(doc.body)
// console.log(doc.createElement("div"))
// let a=doc.body.querySelector("div")
// console.log(a.textContent("hello testing"))

let i=0;
function clickcount() {
    i=i+1
    if (i==1) {
        alert("you clicked the button once")
        
    } else {
        alert(`you clicked the button ${i} times`)   
    }
}