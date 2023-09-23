 $(document).ready(function(){
        $("#left_header").click(function(){
            $(".pane_header").toggle("fast");
            $(this).toggleClass("active");
        })
        $("#header_cancel").click(function(){
            $(".pane_header").toggle("fast");
            $(this).toggleClass("active");
        })
        $("#categories").click(function(){
            $("#header_pane_post3").slideToggle("slow");
            $(this).toggleClass("active");

        });
        $("#right_header_click").click(function(){
            $("#right_header_menu").toggle("fast");
            $(this).toggleClass("active");
        })

    });