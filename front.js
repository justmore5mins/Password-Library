window.onload = () => {
    window.onresize = () => {
        const submitBtn = document.querySelector("#submitBtn");
        submitBtn.addEventListener("click", () => {
            submitBtn.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            console.log(username,password);

            //發送資料到後台
            const data = {
                username: username,
                password: password,
            };
            
            fetch("/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            })
                .then(response => response.json())
                .then(data => console.log(data));
        });
    };
};