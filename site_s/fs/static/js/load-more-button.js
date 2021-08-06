$(document).ready(function(){
 $(".nmooo").slice(0, 4).show();
 
  $("#load").on("click", function(e){
    e.preventDefault();
    $(".nmooo:hidden").slice(0, 4).slideDown();
    if($(".nmooo:hidden").length == 0) {
      $("#load").fadeOut('slow');
    }
  });
  
  })
