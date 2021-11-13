<html> 

<head> 

</head> 

<body style="font-family: Arial, Helvetica, sans-serif; color:#333"> 

    <div id="login" style="border-style: solid; border-color: #333; border-width: 2px; border-radius: 3px; padding: 10px; width:600px;"> 

        <p>Login</p>         

        <br/><br/> Your user name:<br/> 

        <input type="text" id="email" size="35"placeholder="your email address"> 

        <br/> <br/>Password:<br/> 

        <input type="password" id="password" size="35" placeholder="your email address"> 

        <br/> 

        <input type="button" value="Login" style="margin:20px" onclick="login(email.value, password.value)"> 

    </div> 

    <div id="results"></div> 

                   

    <script> 

        function login( email, password) { 

             

            document.getElementById("results").innerHTML = "Logging in..." 

            const baseURL = "https://carlix.herokuapp.com/" 

            var xhttp = new XMLHttpRequest(); 

            xhttp.onreadystatechange = function() { 

                if (this.readyState == 4 && this.status == 200) { 

                   // Typical action to be performed when the document is ready: 

                  document.getElementById("results").innerHTML = xhttp.responseText; 

                }else{ 

                  document.getElementById("results").innerHTML = 'Error: ' + xhttp.responseText; 

                } 

            }; 

            xhttp.open("GET", baseURL + '?user=' + email + '&password=' +password, true); 

            xhttp.send(); 

                 

          

        } 

         

         

        // This just shows the URL as the user types 

        function showURL(value){ 

            document.getElementById("url").innerHTML="https://app.itmplatform.com/" + value; 

        } 

    </script> 

</body> 

</html> 
