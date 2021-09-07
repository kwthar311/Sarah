// Start Clock

var start = new Date();
var s = 1;
var h = 0;
var m = 0;

setInterval(function(){

    let currentTime = new Date();
    
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();

    
    document.getElementById("hour").innerHTML = hours;
    document.getElementById("minute").innerHTML = minutes;
    document.getElementById("second").innerHTML = seconds;


    // elapsed time
    if (s == 60){
        m += 1;
        s = 0;
    }
    if (m == 60){
        m = 0;
        h += 1;
    }

     
    
    document.getElementById("elapsed").innerHTML = h + " : " + m + " : " + s;

    s += 1;

}, 1000);

function startTime(){
    let currentTime = start;
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();
    document.getElementById("start").innerHTML = hours + " : " + minutes + " : " + seconds;

}

// End Clock

var QuestionCounter = 0;
var Depression = 0;
var Anxity = 0;

// append the message in the messages box
function sendMessage(buttonNum = -1){
    
    var x = document.getElementById('textMessage').value;
    document.getElementById('textMessage').value = "";
    if (x === "")
        return;

    if (QuestionCounter === 5){
        alert("Done");
        QuestionCounter = 0;
        document.getElementById('textMessage').style.display = "block";
        document.getElementById('sendButton').style.display = "block";
        return ;
    }

    if (x === "depression"){

        console.log(buttonNum);
        QuestionCounter += 1;
        document.getElementById('textMessage').style.display = "none";
        document.getElementById('sendButton').style.display = "none";

        var _div = document.createElement('div');
        _div.className = "server";

        var pargraph = document.createElement('p');
        var text = document.createTextNode("Do you feel any anxity ??");
        pargraph.appendChild(text);

        _div.appendChild(pargraph);
        _div.appendChild(document.createElement('br'));
               
        var btn1 = document.createElement('button');
        btn1.style.padding = "10px";
        btn1.style.marginTop = "10px";
        btn1.style.marginRight = "10px";
        btn1.style.backgroundColor = "black";
        btn1.style.borderRadius = "5px";
        btn1.style.outlineStyle = "none";
        btn1.style.border = "none";
        btn1.style.color = "white";
        btn1.innerHTML = "Sometimes";

        btn1.onclick = function(){
            document.getElementById('textMessage').value = "depression";
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
            console.log("He selected Sometime, With value of ");
            sendMessage(3);
        };
        
        var btn2 = document.createElement('button');
        btn2.style.padding = "10px";
        btn2.style.marginTop = "10px";
        btn2.style.marginRight = "10px";
        btn2.style.backgroundColor = "black";
        btn2.style.borderRadius = "5px";
        btn2.style.outlineStyle = "none";
        btn2.style.border = "none";
        btn2.style.color = "white";
        btn2.innerHTML = "Always";

        btn2.onclick = function(){
            document.getElementById('textMessage').value = "depression";
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
            console.log("He selected Always, With value of ");
            sendMessage(2);
        };

        var btn3 = document.createElement('button');
        btn3.style.padding = "10px";
        btn3.style.marginTop = "10px";
        btn3.style.backgroundColor = "black";
        btn3.style.borderRadius = "5px";
        btn3.style.outlineStyle = "none";
        btn3.style.border = "none";
        btn3.style.color = "white";
        btn3.innerHTML = "None";

        btn3.onclick = function(){
            document.getElementById('textMessage').value = "depression";
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
            console.log("He selected None, With value of ");
            sendMessage(1);
        };

        _div.appendChild(btn1);
        _div.appendChild(btn2);
        _div.appendChild(btn3);

        console.log("TEST the send function");
        document.getElementById('messageBox').appendChild(_div);
            
        return;
    }
        
    var node = document.createElement('div');
    node.className = "user";
    

    var pargraph = document.createElement('p');
    var text = document.createTextNode(x);
    pargraph.appendChild(text);

    node.appendChild(pargraph);

    document.getElementById('messageBox').appendChild(node);

    var box = document.getElementById('messageBox');
    box.scrollTop = box.scrollHeight;

    var url = '/sendMessage';
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            alert("The response is : " + this.responseText);
        }
    };

    xhttp.open('POST', '/sendMessage', true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("message=".concat(x));
}


// adding the input[text] to event listener (to can click enter button)
var input = document.getElementById('textMessage');
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13){
        event.preventDefault();
        document.getElementById('sendButton').click();
    }
});