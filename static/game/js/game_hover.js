
$(document).ready(function() {
/* HEADER */
$("#logo,#left_header,.carousel-cell img,#icon_b,.card img").hover(function(){
    $(this).css("filter","brightness(110%)");
    }, function(){
    $(this).css("filter","brightness(100%)");
});

$("#header_1,#header_2,#header_4").hover(function(){
    $(this).css("color","var(--green_header)");
    }, function(){
    $(this).css("color","black");
});

$("#right_header_menu p").hover(function(){
    $(this).css("background-color","var(--green_noon)");
    }, function(){
    $(this).css("background-color","white");
});

$(".header_hover .col-12").not("#header_pane_post3 .col-12").hover(function(){
    $(this).css({"background-color":"var(--green_header)","color":"white"});
    }, function(){
    $(this).css({"background-color":"var(--green_slide)","color":"black"});
});

$("#cat_hover,#header_pane_post3").hover(function(){
    $('#cat_hover').css({"background-color":"var(--green_header)","color":"white"});
    $('#header_pane_post3').css({"background-color":"var(--green_header)","color":"white"});
    }, function(){
    $('#cat_hover').css({"background-color":"var(--green_slide)","color":"black"});
    $('#header_pane_post3').css({"background-color":"var(--green_slide)","color":"black"});
});

/* CAROUSEL */
$(".slide-box-shadow h4,.card-body h4").hover(function(){
    $(this).css("color","var(--green_header)");
    }, function(){
    $(this).css("color","white");
});
/* TITLE */
$(".card-body h4").hover(function(){
    $(this).css("color","var(--green_header)");
    }, function(){
    $(this).css("color","black");
});

$(".hover_tag").hover(function(){
    $(this).css("background-color","rgb(144,156,194)");
    }, function(){
    $(this).css("background-color","var(--green_header)");
});

/* POST */
$(".hover-genre").hover(function(){
    $(this).css({"background-color":"rgb(25,103,210)","color":"white"});
    }, function(){
    $(this).css({"background-color":"white","color":"black"});
});

/* VIDEO */
$(".hover_video").hover(function(){
    $(this).css("background-color","rgb(25,103,210)");
    }, function(){
    $(this).css("background-color","rgb(25,25,25)");
});
});
