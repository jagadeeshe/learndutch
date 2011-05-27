
var WordSearch = (function() {
    var inputId = "#word-input";
    var searchId = "#search";
    var formId = "#search-frm";

    var init = function() {
        $(searchId).click(doSearch);
        $(formId).submit(function(){ doSearch(); return false; });
    };

    var doSearch = function() {
        var word = $(inputId).val();
        word = escape(word);
        if (word == '') { return; }
        window.location.pathname = "/word/" + word + "/";
    };

    return {
        "init": init
    };
})();


var SentenceForm = (function(){
    var formId = '#sentence-frm';
    var feedbackId = '#setence-feedback';

    var init = function() {
        if ($(formId)) { 
            $(formId).submit(submitForm);
        }
    };

    var submitForm = function() {
        var options = { 'success': formResponse };
        $(this).ajaxSubmit(options);
        return false;
    };

    var formResponse = function(responseText) {
        $(feedbackId).html(responseText);
    };

    return {
        "init": init
    }
})();
