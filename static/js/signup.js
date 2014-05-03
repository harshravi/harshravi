$(document).ready(function() {
$(".signup").click(function(e) {
e.preventDefault();
$("fieldset#signup_menu").toggle();
$(".signup").toggleClass("menu-open");
document.getElementById("name").focus();
});
$("fieldset#signup_menu").mouseup(function() {
return false
});
$(document).mouseup(function(e) {
if($(e.target).parent("a.signup").length==0) {
$(".signup").removeClass("menu-open");
$("fieldset#signup_menu").hide();
}
});
});
