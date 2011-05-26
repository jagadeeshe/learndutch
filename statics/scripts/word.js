
var WordSearch = (function() {
    var viewIds = {
        inputId: "#word-input",
        searchId: "#search",
        formId: "#search-frm"
    };

    var init = function() {
        attachHandlers();
    };

    var attachHandlers = function() {
        $(viewIds.searchId).click(doSearch);
        $(viewIds.inputId).keypress(function(event) {
            if(event.keyCode == '13') { doSearch(); }
        });
        $(viewIds.formId).submit(function(){ return false;});
    };

    var doSearch = function() {
        var word = $(viewIds.inputId).val();
        word = escape(word);
        if (word == '') { return; }
        window.location.pathname = "/word/" + word + "/";
    };

    return {
        "init": init
    };
})();


var SetenceForm = (function(){
    var viewIds = {
        formId: '#sentence-frm',
        wordId: '#id_ref_word_id',
        feedbackId: '#setence-feedback'
    };

    var init = function() {
        attachHandlers();
    };

    var attachHandlers = function() {
        if ($(viewIds.formId)) { 
            $(viewIds.formId).submit(submitForm);
        }
    };

    var submitForm = function(event) {
        event.preventDefault(); 

        var form = $( this );
        var url = form.attr( 'action' );
        var sentence = form.find('textarea[name="sentence"]').val();
        var wordId = form.find('input[name="ref_word_id"]').val();
        var token = form.find('input[name="csrfmiddlewaretoken"]').val();

        $.post( url, { csrfmiddlewaretoken: token, ref_word_id: wordId, sentence: sentence})
        .success( function( data ) {
            $(viewIds.feedbackId).html(data);
        });
    };

    return {
        "init": init
    }
})();