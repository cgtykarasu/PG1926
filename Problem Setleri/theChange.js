function init() {
    var x = document.getElementById("amountOfMoney");
    var result = document.getElementById("result");
    x.onkeyup = function(e) {
    var val = this.value*100;

    var oneLi = Math.floor(val/100);
    val = val%100;

    var fiftyKr = Math.floor(val/50);
    val = val%50;

    var twentyFiveKr = Math.floor(val/25);
    val = val%25;

    var tenKr = Math.floor(val/10);
    val = val%10;

    var fiveKr = Math.floor(val/5);
    val = val%5;

    var oneKr = Math.floor(val/1);
    val = val%1;

    result.innerHTML = "1 Lira : " + oneLi + 
    "<br /><hr> 50 Kuruş : " + fiftyKr + 
    "<br /><hr> 25 Kuruş : " + twentyFiveKr + 
    "<br /><hr> 10 Kuruş : " + tenKr + 
    "<br /><hr> 5 Kuruş : " + fiveKr + 
    "<br /><hr> 1 Kuruş : " + oneKr;
    }
}
window.onload = init;


