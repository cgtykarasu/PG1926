function isPrime(num) {
    var prime = num != 1;
    for(var i=2; i<num; i++) {
        if(num % i == 0) {
            prime = false;
            break;
        }
    }
    return prime;
}

function init() {
    var input = document.getElementById("input_num");
    var result = document.getElementById("result");
    input.onkeyup = function(e) {
        var val = this.value;
        if(val == "") {
            result.className = "";
            result.innerHTML = "";
            return;
        }
        if(/\D/.test(val)) {
            result.className = "invalid";
            result.innerHTML = "Invalid!";
        } else {
            result.innerHTML = 
            isPrime(val) ? "Yes, it's a Prime Number" : "No, it's not a Prime Number";
            result.className = isPrime(val) ? "prime" : "notPrime";
        }
    };
}

window.onload = init;
