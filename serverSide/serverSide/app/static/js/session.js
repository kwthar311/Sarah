
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
    if (x == "")
        return;


        if (x == "Would ask you some questions ?"){
            
            var _div = document.createElement('div');
            _div.className = "server";

            var pargraph = document.createElement('p');
            var text = document.createTextNode( x);
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
            btn1.innerHTML = "Yes";

            btn1.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Sometime, With value of ");
                sendMessage(1);
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
            btn2.innerHTML = "No";

            btn2.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Always, With value of ");
                sendMessage(0);
            };

            _div.appendChild(btn1);
            _div.appendChild(btn2);

            document.getElementById('messageBox').appendChild(_div);
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
            return;
        }
        else if (window.Depression == 1 && x != "depression"){
            var _div = document.createElement('div');
            _div.className = "server";

            var pargraph = document.createElement('p');
            var text = document.createTextNode( x);
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
            btn1.innerHTML = "Not ones";

            btn1.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Sometime, With value of ");
                sendMessage(0);
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
            btn2.innerHTML = "Less than one week";

            btn2.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Always, With value of ");
                sendMessage(1);
            };

            var btn3 = document.createElement('button');
            btn3.style.padding = "10px";
            btn3.style.marginTop = "10px";
            btn3.style.marginRight = "10px";
            btn3.style.backgroundColor = "black";
            btn3.style.borderRadius = "5px";
            btn3.style.outlineStyle = "none";
            btn3.style.border = "none";
            btn3.style.color = "white";
            btn3.innerHTML = "More than one week";

            btn3.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected None, With value of ");
                sendMessage(2);
            };

            var btn4 = document.createElement('button');
            btn4.style.padding = "10px";
            btn4.style.marginTop = "10px";
            btn4.style.backgroundColor = "black";
            btn4.style.borderRadius = "5px";
            btn4.style.outlineStyle = "none";
            btn4.style.border = "none";
            btn4.style.color = "white";
            btn4.innerHTML = "Mostly every day";

            btn4.onclick = function(){
                document.getElementById('textMessage').value = "depression";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected None, With value of ");
                sendMessage(3);
            };

            _div.appendChild(btn1);
            _div.appendChild(btn2);
            _div.appendChild(btn3);
            _div.appendChild(btn4);

            document.getElementById('messageBox').appendChild(_div);
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
        }
        else if (window.Anxity == 1 && x != "anxity"){
            var _div = document.createElement('div');
            _div.className = "server";

            var pargraph = document.createElement('p');
            var text = document.createTextNode( x);
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
            btn1.innerHTML = "Never";

            btn1.onclick = function(){
                document.getElementById('textMessage').value = "anxity";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Sometime, With value of ");
                sendMessage(0);
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
            btn2.innerHTML = "Some days";

            btn2.onclick = function(){
                document.getElementById('textMessage').value = "anxity";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected Always, With value of ");
                sendMessage(1);
            };

            var btn3 = document.createElement('button');
            btn3.style.padding = "10px";
            btn3.style.marginTop = "10px";
            btn3.style.marginRight = "10px";
            btn3.style.backgroundColor = "black";
            btn3.style.borderRadius = "5px";
            btn3.style.outlineStyle = "none";
            btn3.style.border = "none";
            btn3.style.color = "white";
            btn3.innerHTML = "More than half of the days";

            btn3.onclick = function(){
                document.getElementById('textMessage').value = "anxity";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected None, With value of ");
                sendMessage(2);
            };

            var btn4 = document.createElement('button');
            btn4.style.padding = "10px";
            btn4.style.marginTop = "10px";
            btn4.style.backgroundColor = "black";
            btn4.style.borderRadius = "5px";
            btn4.style.outlineStyle = "none";
            btn4.style.border = "none";
            btn4.style.color = "white";
            btn4.innerHTML = "Almost everyday";

            btn4.onclick = function(){
                document.getElementById('textMessage').value = "anxity";
                var box = document.getElementById('messageBox');
                box.scrollTop = box.scrollHeight;
                console.log("He selected None, With value of ");
                sendMessage(3);
            };

            _div.appendChild(btn1);
            _div.appendChild(btn2);
            _div.appendChild(btn3);
            _div.appendChild(btn4);

            document.getElementById('messageBox').appendChild(_div);
            var box = document.getElementById('messageBox');
            box.scrollTop = box.scrollHeight;
        }
    
    
    if (window.Depression == 0 && window.Anxity == 0){
        var node = document.createElement('div');
        if (buttonNum == 5000)
           node.className = "server";
        else 
          node.className = "user";
    

        var pargraph = document.createElement('p');
        var text = document.createTextNode(x);
        pargraph.appendChild(text);

        node.appendChild(pargraph);

        document.getElementById('messageBox').appendChild(node);

        var box = document.getElementById('messageBox');
        box.scrollTop = box.scrollHeight;
    }

    if (buttonNum == 5000 || buttonNum == 50) 
        return;

    if (buttonNum != -1)
        x = buttonNum;

    var url = '/sendMessage';
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            if (this.responseText == "depression"){
                alert("Start")
                Depression = 1;
                document.getElementById('textMessage').style.display = "none";
                document.getElementById('sendButton').style.display = "none";
                document.getElementById('textMessage').value = "Would ask you some questions ?";
                sendMessage();
            }
            else if (this.responseText == "anxity") {
                alert("start Anxity");
                Anxity = 1;
                document.getElementById('textMessage').style.display = "none";
                document.getElementById('sendButton').style.display = "none";
                document.getElementById('textMessage').value = "Would ask you some questions ?";
                sendMessage();
            }
            else if (this.responseText.includes("endofsurvey")){
                alert("End of survey\n" + this.responseText);
                Depression = 0;
                Anxity = 0;
                document.getElementById('textMessage').style.display = "block";
                document.getElementById('sendButton').style.display = "block";
                QuestionCounter = 100;
                document.getElementById('textMessage').value = "Done!";
                sendMessage(5000);
            }
            else {
                
                QuestionCounter = 100;
                document.getElementById('textMessage').value = this.responseText;
                sendMessage(5000);
            }
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

// load messages
function loadMessages(){
    alert("In the load messages");

    var url = "/loadMessages";
   
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){

            var data = this.responseText.split('|');
            alert(data)
            data.forEach(element => {
                var msg = element.split('>');
                var node = document.createElement('div');
                node.className = String(msg[1]);
                var pargraph = document.createElement('p');
                var text = document.createTextNode(msg[0]);
                pargraph.appendChild(text);
                node.appendChild(pargraph);
                document.getElementById('messageBox').appendChild(node);

            });
        }
    };
    xhttp.open('POST', url, true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("message=From LoadMessage function in userHome.js");

}