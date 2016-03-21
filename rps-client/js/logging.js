function loginWithToken() {
    var token = $("#inputToken").val();
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: "http://localhost:8080/tokens",
        contentType: 'application/json',
        data: {'token': token},
        success: function(data){
            session_info['token'] = token;
            session_info['sys_name'] = data['name'];
            onLogged();
        }
    });
}

function onLogged() {
    $('#login-wrapper').fadeOut(100, function() {
        $('#wrapper').show();
    });
}

