    $('#next').click(function(){
    var catid;
    page = $(this).attr("page");
     $.get('/article/article_footer/', {page: page}, function(data){
               $('#dynamic_tab').html(data);
              
           });
});