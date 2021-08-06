$( document ).ready(function() {
    	// let's Hide Items
   var slideIndex = 0;
      showSlides();
      
      function showSlides() {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dotss");
        for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";  
        }
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}    
        for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" activess", "");
        }
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " activess";
        setTimeout(showSlides, 10000); // Change image every 2 seconds
      }
     
    });

