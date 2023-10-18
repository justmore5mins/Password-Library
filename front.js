const form = document.querySelector("form");
const loginButton = document.querySelector("input[type='submit']");

loginButton.addEventListener("click",() =>{
    const username = form.querySelector("input[name='username']").value;
    const passowrd = form.querySelector("input[name='password']").value;
    form.reset();
    console.log("user ",username,"login by password: ",passowrd)
})