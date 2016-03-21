var session_info = {
    'token': '',
    'sys_name': ''
};

function locationHashChanged() {
    if (location.hash === "#logged") {
        loginWithToken();
    }
    if (location.hash === "#moncpu") {
        loadMonitoring();
    }
}

window.onhashchange = locationHashChanged;
