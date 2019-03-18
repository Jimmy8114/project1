
function myFunction1(){
    //document.getElementById("content").innerHTML = "这是电脑"
    $.ajax({
      url:"computer.html"
    });
    //location.href = "{% url 'app2:computer' %}";
}

function myFunction2(){
    //document.getElementById("content").innerHTML = "这是手机"
    $.ajax({
      url:"iphone.html"
    });
    //location.href = "{% url 'app2:iphone' %}";
}

function gotoPage(){
         var pageNum = document.getElementById("pageNum").value;
         $.ajax({
             type: "GET",
             url: "/app2/computer/",
             data: { page: pageNum },
         });
    }