// const text_input = document.getElementById("text-input");
// const submit = document.getElementById("submit-btn");

// submit.addEventListener('click',  () => { //async
//     const text = textInput.value;
//     console.log(text);
//     preventDefault();
// //     const response = await fetch('fjksl;fdsjfl the HTTPS route for backend') //change when api route obtained
// })
window.onload = function(){
    
    var a = document.getElementById("myDiv")
    if(a){
        a.addEventListener("mousemove", function(event) {
            myFunction(event);
        });   
    }
}

document.getElementById("myDiv").addEventListener("mousemove", function(event) {
    myFunction(event);
});  
  
  function myFunction(e) {
    let img = document.getElementById("MONKEY");
    let offsetX = e.clientX;
    let offsetY =  e.clientY;

    let coor = "Coordinates: (" + x + "," + y + ")";
    document.getElementById("text-input").innerHTML = coor;

    img.style.left = offsetX + "px";
    img.style.top= offsetY + "px";

 }