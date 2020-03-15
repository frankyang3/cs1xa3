$(document).ready(function(){
      $(".exp").hide();
      $(".comp").hide();
      $(".edu").hide();
      $("#experiences").click(function(){
        $(".exp").toggle(100, function(){
                if($(this).is(":visible")){
                  $("#experiences").removeClass("w3-hover-opacity")
                } else{
                  $("#experiences").addClass("w3-hover-opacity")
                }
        });
      });
      $("#compProg").click(function(){
        $(".comp").toggle(100, function(){
                if($(this).is(":visible")){
                  $("#compProg").removeClass("w3-hover-opacity")
                } else{
                  $("#compProg").addClass("w3-hover-opacity")
                }
        });
      });
      $("#education").click(function(){
        $(".edu").toggle(100, function(){
                if($(this).is(":visible")){
                  $("#education").removeClass("w3-hover-opacity")
                } else{
                  $("#education").addClass("w3-hover-opacity")
                }
        });
        
      });
  
      
    });