const text_input = document.getElementById("text-input");
const submit = document.getElementById("submit-btn");

submit.addEventListener('click',  () => { //async
    const text = textInput.value;
    console.log(text);
    preventDefault();
//     const response = await fetch('fjksl;fdsjfl the HTTPS route for backend') //change when api route obtained
})

