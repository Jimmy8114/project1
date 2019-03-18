function loadList(){
            $.ajax({
                 method: "GET",
                 url: "/api/getlist/",
                 dataType: "json",
                 success: function(data) {
                     for (i=0;i<data.length;i++){
                        $("#human-table-body").append(
                           ' <tr>\n' +
                           '   <th scope="col">' + data[i]['humanName'] + '</th>\n' +
                           '   <th scope="col">' + data[i]['humanAge'] + '</th>\n' +
                           ' </tr>'
                        )
                     }
                 }
             });
}

function modify(){
                 var pid = {{ pk|safe }};
                 var purl = "/api/human/" + pid + "/";
                 var i = pid - 1;
                 $.ajax({
                     url: "/api/human/1/",
                     method: "post",
                     data: { humanName: $("#humanName").val(), humanAge: $("#humanAge").val() },
                     dataType: "json",
                     success: function(data){
                         $("#humanName").text(data[i]['humanName']);
                         $("#humanAge").text(data[i]['humanAge']);
                     }
                 });
}