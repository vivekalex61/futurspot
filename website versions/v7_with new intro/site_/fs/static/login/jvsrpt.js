
function log() {
	var fieldValue1 = 
                document.getElementById('user').value; 
  
            localStorage.setItem('username', fieldValue1); 

     var fieldValue2 = 
                document.getElementById('pass').value; 
  
            localStorage.setItem('password', fieldValue2); 

var username=localStorage.getItem("username");
var password=localStorage.getItem("password");
       if(username=="future" && password== "wdvwr5566")  
       {location.href = "platform.html";}
   else
   	{alert("Username/password is wrong!");}
        
     
    };