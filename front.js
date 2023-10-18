window.onload = () => {
    window.onresize = () => {
        const submitBtn = document.querySelector("#submitBtn");
        submitBtn.addEventListener("click", () => {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        console.log("user ",username,"log in by ",password)
        });
      };
  };    