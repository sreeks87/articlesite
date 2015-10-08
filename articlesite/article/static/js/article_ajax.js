    $('#next').click(function(){
    var catid;
    page = $(this).attr("page");
     $.get('/rango/like_category/', {page: page}, function(data){
               $('#dynamic_tab').html(data);
              
           });
});