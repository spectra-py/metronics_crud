console.log("This is jquery")

$(document).ready(function(){
    $("#data").click(function(){
        console.log("hello")
        $("#jrqst").load("/static/jq.txt");

    });
});

$(document).ready(function(){

    $("#popBtn").click(function(){

      $(function () {

            $.ajax({

              type: 'GET',

              cache: false,

              url: "https://jsonplaceholder.typicode.com/posts",

              complete: function (res) {

                my_data = res.responseText;

                console.log(my_data);

                var jsonObject = $.parseJSON(my_data);

                $.each(jsonObject, function(i,obj){

                    var data = obj.title;

                    console.log(obj.title);

                    $("#list1").append('<li>'+obj.title+'</li>');

                });

              }

            });

          });

    })

});
        
    
        


                
               
             
                 
     