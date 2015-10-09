    $('#next').click(function(){
    var catid;
    page = $(this).attr("page");
     $.get('/article/like_category/', {page: page}, function(data){
               $('#dynamic_tab').html(data);
              
           });
});