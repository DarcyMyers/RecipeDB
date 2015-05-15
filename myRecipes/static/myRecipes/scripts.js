/**
 * Created by Darc on 5/14/15.
 */
$(document).ready(function(){
    $(function() {
        // the jqueryUI accordion method
        $( "#accordionForm" ).accordion(
        	// the heightStyle option with the "content" parameter causes each tab to be the height of its content
            { heightStyle: "content" }
        );
    });
});