
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