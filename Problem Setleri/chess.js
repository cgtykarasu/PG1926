var tablo = document.getElementById("table");
var tableHorizontal = [];
var tableVertical = [];
var buton = [];
var letters = ["A","B","C","D","E","F","G","H"];
var numbers = ["8","7","6","5","4","3","2","1"];
document.body.appendChild(tablo);
function onClik(a){
    var x = document.getElementById("div");
    x.innerHTML = a;
}

for (let i = 0; i < 9; i++) {
    tableVertical[i] = tablo.appendChild(document.createElement("TR"));
    for (let j = 0; j < 9; j++) {
        tableHorizontal[j] = document.createElement("TD");
        tableVertical[i].appendChild(tableHorizontal[j]);
    }

    for (let i = 0; i < 9; i++) {
            buton[i] = document.createElement("button");
            tableHorizontal[i].appendChild(buton[i]);
            buton[i].innerHTML = "‏‏‎";
            buton[i].setAttribute("class","buton");
    }

    for (let e = 1; e < 9; e++) {
        for (let f = 1; f < 9; f++) {
            if (i+1 == 9-f) {
                buton[e].setAttribute("id",letters[e-1]+numbers[8-f]);
                buton[e].setAttribute("onclick","onClik("+"'"+letters[e-1]+numbers[8-f]+"'"+")");
                if ((e % 2 == 1 && f % 2 == 1) || (e % 2 == 0 && f % 2 == 0)) {
                    buton[e].setAttribute("class","blue01");
                }
                else{
                    buton[e].setAttribute("class","blue02");
                }
            }
        }
    }

    for (let c = 0; c < 8; c++) {
        if (i == 8) {
            buton[c+1].innerHTML = letters[c];
        }
                
    }

    for (let d = 0; d < 8; d++) {
        if (d == i) {
            buton[0].innerHTML = numbers[d];
        }
    }
}