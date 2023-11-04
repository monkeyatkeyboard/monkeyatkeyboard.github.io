// const text_input = document.getElementById("text-input");
// const submit = document.getElementById("submit-btn");
// const result = document.getElementById("");

// submit.addEventListener('click',  async (event) => {
//     const text = text_input.value;
//     console.log(text);
//     event.preventDefault();
//     text_input.value = "";


//     const response = await fetch('./BackEnd', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//         },
//         body: `text=${text}`,
//     });

//     if (response.ok) {
//         const data = await response.json();
//         resultElement.innerHTML = `Processed Result: ${data.result}`;
//     } else {
//         resultElement.innerHTML = 'Error processing text.';
//     }
// });
