window.onload = () => {
    window.onresize = () => {
        const submitBtn = document.querySelector("#submitBtn");
        submitBtn.addEventListener("click", () => {
            submitBtn.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            console.log(username,password);
        });
    };
};    