
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

/**
 * 
 * @param formId  - formId to which ajax submit is attached
 * @param options - map containing
 * {
 *  'success': array of callbacks called with result
 *  'error': callback when called with error message
 * }
 * 
 */
var FormController = function(formId, options) {

    var defaults = {
            success: [],
            error: function() {}
    };

    var formResponse = function(data) {
        if (data.success) {
            for(var i=0; i<options.success.length; i++) {
                var  cb = options.success[i];
                cb(data.result);
            }
        } else {
            options.error(data.messages);
        }
    };

    var submitHandler = function () {
        var options = {'success': formResponse};
        $(this).ajaxSubmit(options);
        return false;
    };

    /*for (var name in defaults) {
        if (options[name] == 'undefined') {
            options[name] = defaults[name];
        }
    }*/
    //if (typeof options.success ==) TODO: type check
    $(formId).submit(submitHandler);
}

var SentenceListView = function(viewLocator) {

    var addItem = function(text) {
        $.tmpl("<li>${text}</li>", {'text':text}).appendTo(viewLocator);
    };

    var removeItem = function() { };

    return {
        "addItem": addItem,
        "removeItem": removeItem
    };
};

var SentenceForm = (function(){
    var formId = '#sentence-frm';
    var feedbackId = '#setence-feedback';

    var success = function(sentence) {
        SentenceListView('.sentence-list').addItem(sentence);
        $(formId).find('textarea[name=sentence]').val('');
        $(formId).find('textarea[name=sentence]').focus();
    };

    var error = function(messages) {
        $(feedbackId).html(messages[0]);
    };

    var init = function() {
        FormController(formId, {
            success: [success],
            error: error
        });
    };

    return {
        "init": init
    }
})();

var TagListView = function(viewLocator) {

    var addItem = function(tag) {
        $.tmpl('<li><a href="${url}">${tag}</a></li>', tag).appendTo(viewLocator);
    };

    var removeItem = function() {};

    return {
        "addItem": addItem,
        "removeItem": removeItem
    };
};

var TagForm = (function(){
    var formContainerId = ".tag-frm-ctr";

    var success = function(tag) {
        TagListView('.tag-list').addItem(tag);
        $(formContainerId).hide();
    };

    var error = function(messages) {
        $("#tag-feedback").html(messages[0]);
    };

    var init = function() {
        $(".action-add-tag").click(function() { $(formContainerId).show(); });

        FormController("#tag-frm", {
            'success': [success],
            'error': error
        });
    };

    return {
        "init": init
    };
})();


var WordForm = (function() {

    var init = function() {
        $("#id_word").focus();
    };

    return {
        "init": init
    }
})();