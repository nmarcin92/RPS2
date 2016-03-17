function locationHashChanged() {
    if (location.hash === "#logged") {
        loginWithToken();
    }
    if (location.hash === "#monitoring") {
        var contentWrapper = $("#page-content-wrapper");
        contentWrapper.empty();
        contentWrapper.load("html/monitoring.html");
    }
}

window.onhashchange = locationHashChanged;

$('#date-range-picker').find('.input-daterange').datepicker({
});