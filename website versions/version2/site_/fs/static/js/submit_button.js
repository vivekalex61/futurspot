$( document ).ready(function() {
    	// let's Hide Items
    	$( ".cc-contactpop form").hide();
    	$( ".cc-contactpop i").hide(); 
    	$( ".cc-contactpop p").hide();
    	// Show on elements ".slideDown"
    	$( ".cc-contactpop" ).click(function() {
    		$( ".cc-contactpop form").slideDown(500)
    		$( ".cc-contactpop p").slideDown(500)
    		$( ".cc-contactpop i").slideDown(500)
    	});
    	// Close Hidden Part
    	$( ".cc-contactpop i" ).click(function() {
    		$(this).slideUp(500)
    			$( ".cc-contactpop p").slideUp(500)
    			$( ".cc-contactpop form").slideUp(500)
    		return false
    	});
     
    });

