// select skills selector
let totalSessions = document.querySelectorAll(".sessions .session-box .session-progress span");

totalSessions.forEach(bar => {
    bar.style.width = bar.dataset.progress;
});

// end select skills selector


// show password function
function showPassword(){
    var x = document.getElementById('myPassword');
    if (x.type === "password"){
        x.type = "text";
    }
    else {
        x.type = "password";
    }
}

// end show password function

// Edit user information
function saveChanges(){
    var name = document.getElementById('myName').value;
    var user_name = document.getElementById('myUserName').value;
    var email = document.getElementById('myEmail').value;
    var age = document.getElementById('myAge').value;
    var password = document.getElementById('myPassword').value;

    var msg = "name=".concat(name).concat("&email=").concat(email).concat("&userName=").concat(user_name).concat("&age=").concat(age).concat("&password=").concat(password);
    console.log(msg);

    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/saveChanges', true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send(msg);
}

// End Edit user information