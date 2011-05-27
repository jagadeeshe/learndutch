
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

var SentenceListView = function(viewLocator) {

    var addItem = function(text) {
        $.tmpl("<li>${text}</li>", {'text':text}).appendTo(viewLocator);
    };

    return {
        "addItem": addItem
    };
};

var SentenceForm = (function(){
    var formId = '#sentence-frm';
    var feedbackId = '#setence-feedback';
    var view = SentenceListView('.sentence-list');

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

    var formResponse = function(data) {
        if (data.success) {
            view.addItem(data.result);
            $(formId).find('textarea[name=sentence]').val('');
            $(formId).find('textarea[name=sentence]').focus();
        } else {
            $(feedbackId).html(data.message[0]);
        }
    };

    return {
        "init": init
    }
})();
