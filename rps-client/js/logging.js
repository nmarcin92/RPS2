function loginWithToken() {
    var token = $("#inputToken").val();
    var data1 = {'system_name': token};
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: "http://localhost:8080/tokenss",
        contentType: 'application/json',
        data: {'token': token},
        success: function(data){
            alert(data);
        }
    });
}

