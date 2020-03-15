$(document).ready(function(){
      $("#day").click(function(){
        if($("div").hasClass("w3-light-grey")){
          $("div").addClass("w3-black")
          $("div").removeClass("w3-light-grey")
          $("#day").addClass("w3-blue")
          $("#day").removeClass("w3-black")
        } else if ($("div").hasClass("w3-black")){
          $("div").addClass("w3-light-grey")
          $("div").removeClass("w3-black")
          $("#day").addClass("w3-blue")
          $("#day").removeClass("w3-light-grey")

          $(".about").removeClass("w3-light-grey")

          $("#nav").removeClass("w3-light-grey")
          $("#nav").addClass("w3-blue")

          $("#navDemo").removeClass("w3-light-grey")
          $("#navDemo").addClass("w3-blue")
         

        }
      });
    });
// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
    } else { 
      x.className = x.className.replace(" w3-show", "");
    }
  }