var current_username = ""
verified = false

function toggleActive(clickedButton) {
    const buttons = document.querySelectorAll('#login-signup button');

    buttons.forEach(button => {
        button.style.backgroundColor = "#F97300";
        button.style.color = "black"; 
    });
    
    var button = document.getElementById(clickedButton)
    button.style.backgroundColor="#000000cc"
    button.style.color="#E2DFD0"

    if (clickedButton === "select-signup"){
        var signup_page = document.getElementById("signup-inputs")
        var login_page = document.getElementById("login-inputs")

        signup_page.style.display = "flex"
        login_page.style.display = "none"
    } else if (clickedButton === "select-login"){
        var signup_page = document.getElementById("signup-inputs")
        var login_page = document.getElementById("login-inputs")

        signup_page.style.display = "none"
        login_page.style.display = "flex"
    }
}


function ForgotPassword (){
    var e1 = document.getElementById("login-signup")
    var e2 = document.getElementById("login-inputs")
    var e3 = document.getElementById("signup-inputs")
    var fe = document.getElementById("forgot-password-email")

    e1.style.display = "none"
    e2.style.display = "none"
    e3.style.display = "none"
    fe.style.display = "flex"
}

function ForgotPasswordSubmitEmail (){
    var fe = document.getElementById("forgot-password-email")
    var fc = document.getElementById("forgot-password-code")
    fe.style.display = "none"
    fc.style.display = "flex"
}

function ForgotPasswordSubmitCode (){
    var fc = document.getElementById("forgot-password-code")
    var fp = document.getElementById("forgot-password")
    fc.style.display = "none"
    fp.style.display = "flex"
}

function backtologin () {
    var e1 = document.getElementById("login-signup")
    var e2 = document.getElementById("login-inputs")
    var fp = document.getElementById("forgot-password")
    var ctl = document.getElementById("continue-to-login")
    var fptl = document.getElementById("forgot-password-backtologin")

    e1.style.display = "flex"
    e2.style.display = "flex"
    fp.style.display = "none"
    ctl.style.display = "none"
    fptl.style.display = "none"
}

function showresetnote(){
    var e1 = document.getElementById("login-signup")
    var e2 = document.getElementById("login-inputs")
    var fp = document.getElementById("forgot-password")
    var fptl = document.getElementById("forgot-password-backtologin")

    e1.style.display = "none"
    e2.style.display = "none"
    fp.style.display = "none"
    fptl.style.display = "flex"
}

function postsignup (){
    var signup = document.getElementById("signup-confirm-inputs")
    signup.style.display = "none"
    var ctl = document.getElementById("continue-to-login")
    ctl.style.display = "flex"
}

function login() {
    var username = document.getElementById("login-username").value;
    var password = document.getElementById("login-password").value;
    var loginlog = document.getElementById("login-log")

    document.getElementById("loading").style.display = "flex";

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    }).then(response => {
        if (response.ok) {
            window.location.href = '/home';
        } else {
            return response.json().then(data => {
                loginlog.innerText = data.error;
            });
        }
    }).catch(error => {
        console.error('Error:', error);
    }).finally(() => {
        document.getElementById("loading").style.display = "none";
    });
    
}

function signup() {
    var username = document.getElementById("signup-username").value;
    var email = document.getElementById("signup-email").value;
    var password = document.getElementById("signup-password").value;
    var confirm_password = document.getElementById("signup-confirm-password").value;
    
    var e1 = document.getElementById("login-signup")
    var e2 = document.getElementById("login-inputs")
    var e3 = document.getElementById("signup-inputs")
    var fe = document.getElementById("forgot-password-email")
    var validate = document.getElementById("signup-confirm-inputs")

    var signuplog = document.getElementById("signup-log");

    if (password === confirm_password){

        document.getElementById("loading").style.display = "flex"

        fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username, email: email, password: password })
        }).then(response => {
            if (response.ok) {
                e1.style.display = "none"
                e2.style.display = "none"
                e3.style.display = "none"
                fe.style.display = "none"
                validate.style.display = "flex"

                current_username = username
                
            } else {
                return response.json().then(data => {
                    signuplog.innerText = data.error;
                });
            }
        }).catch(error => {
            console.error('Error:', error);
        }).finally(() => {
            document.getElementById("loading").style.display = "none";
        });
    } else {
        signuplog.innerText = "Passwords do not match.";
    }
}

function confirm_signup() {

    var signup_confirm_log = document.getElementById("signup-confirm-log")
    var validation_code = document.getElementById("vcode").value

    document.getElementById("loading").style.display = "flex"

    fetch('/validate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: current_username, validation_code: validation_code})
    }).then(response => {
        if (response.ok) {
            verified = true
            postsignup()
        } else {
            return response.json().then(data => {
                signup_confirm_log.innerText = data.error;
            });
        }
    }).catch(error => {
        console.error('Error:', error);
    }).finally(() => {
        document.getElementById("loading").style.display = "none";
    });
}

function resend(){

    document.getElementById("loading").style.display = "flex"

    fetch('/resend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: current_username})
    }).then(response => {
        if (response.ok) {
            document.getElementById("signup-confirm-log").innerText = "A new Verification Code has been sent."
        } else {
            return response.json().then(data => {
                document.getElementById("signup-confirm-log").innerText = data.error;
            });
        }
    }).catch(error => {
        console.error('Error:', error);
    }).finally(() => {
        document.getElementById("loading").style.display = "none";
    });
}