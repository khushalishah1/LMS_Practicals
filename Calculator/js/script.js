// take the screen id selector
let screen = document.querySelector('#screen');

// take all the btn class selector
let btn = document.querySelectorAll(".btn");
let x = 0;

//for button press
for (let item of btn) {
    item.addEventListener('click', (e) => {
        btntext = e.target.innerText;
        //console.log(btntext);

        if (btntext == 'X')
            btntext = '*';

        if (btntext == '÷')
            btntext = '/';

        if (btntext == 'mod')
            btntext = '%';

        if (btntext == 'xy')
            btntext = '**';
        screen.value += btntext;
    });
}

// for press button through keyboard
var key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '%', ')', '(', 'enter'];
function checkPressedKey(e) {
    let val = e.key
    for (let i = 0; i < key.length; i++) {
        if (key[i] == val) { return true; }
        else if ("Enter" == val) { equal(); }
    }
    return false;
}

// = function
function equal() {

    try {
        screen.value = eval(screen.value)
    }
    catch (error) {
        screen.value = "error";
    }
}

//sin function
function sin() {
    screen.value = Math.sin(screen.value);
}

//cos function
function cos() {
    screen.value = Math.cos(screen.value);
}

//tan function
function tan() {
    screen.value = Math.tan(screen.value);
}

//cot function
function cot() {
    screen.value = Math.cot(screen.value)
}
//x^2 function
function power() {
    screen.value = Math.pow(screen.value, 2);
}

//one upon x function
function oneuponx() {
    screen.value = Math.pow(screen.value, -1);
}

//square root function
function sqrt() {
    screen.value = Math.sqrt(screen.value);
}

//10^x function
function tentox() {
    screen.value = Math.pow(10, screen.value)

}

//clear all function on screen
function clearall() {
    screen.value = '';
}

//pi value function
function pi() {
    if (screen.value == "") {
        screen.value = Math.PI + '*';
    }
    else {
        screen.value = screen.value * Math.PI;
    }
}

//e value function
function evalue() {
    if (screen.value == "") {
        screen.value = 2.71828182846 + '*';
    }
    else {
        screen.value = screen.value * 2.71828182846;
    }
}

//factorial  function
function fact(n) {
    let ans = 1;
    if (n == 0 || n == 1)
        screen.value = 1;

    else if (n > 1) {
        for (let i = n; i >= 1; i--) {
            ans = ans * i;
        }

        screen.value = ans;
    }
}


//backspace function
function backspace() {
    screen.value = screen.value.substr(0, screen.value.length - 1);
}

//log value function
function log() {
    screen.value = Math.log10(screen.value);
}

//ln function
function ln() {
    screen.value = Math.log(screen.value);
}


//mplus function function
function mplus() {

    x += eval(screen.value);
    console.log(x);
}

//mminus function function
function mminus() {

    x -= eval(screen.value);
    console.log(x);
}

//ms->store value in console
function ms() {
    x = screen.value;
    console.log(screen.value);
}

//mr->read the last value of console
function mr() {
    screen.value = x;
}

//mc function->clear log 
function mc() {
    console.clear();
}

//|x| function
function positive() {
    screen.value = Math.abs(screen.value);
}

//exp function
function exp() {
    screen.value = Math.exp(screen.value);
}

//plus minus function
function plusminus() {
    if (screen.value > 0)
        screen.value = -screen.value;
    else
        screen.value = Math.abs(screen.value);

}

//radian to degree convertion function
function radToDeg(rad) {
    screen.value = rad * (180.0 / Math.PI);
}

//covert to floor value function
function floor() {
    screen.value = Math.floor(screen.value);
}

//convert to ceil value function
function ceil() {
    screen.value = Math.ceil(screen.value);
}

//sign value function
function sign() {
    screen.value = Math.sign(screen.value);
}