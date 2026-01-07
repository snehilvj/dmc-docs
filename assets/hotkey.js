hotkeys('ctrl+k, cmd+k', function (event, handler){
    event.preventDefault();
    event.stopPropagation();
    document.getElementById("select-component").focus()
});
