(function() {
    $('#submit-add').click(function() {
        let twitter = $('input[name=Twitter-Handle]').val();
        console.log(twitter);
        let lower = parseInt($('input[name=Lower-Price]').val(), 10);
        let upper = parseInt($('input[name=Upper-Price]').val(), 10);

        // call add_person from api.js
        add_person(twitter, lower, upper);
    })
})();
