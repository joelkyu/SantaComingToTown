function indexPage () {
    fetch(`http://52.54.115.82:8080`, {method: "GET"})
    .then(
        function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
            return;
        }
        // Examine the text in the response
        console.log(response);
        response.json().then(function(data) {

            return data
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
}

function add_person(twitter_handle, lower_price, upper_price) {
    fetch(`http://52.54.115.82:8080/add`, {
        method: "POST",
        headers: {
            "accept": 'application/json',
            twitter_handle, lower_price, upper_price
        }
    })
    .then(
        function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
            return;
        }
        // Examine the text in the response
        response.json().then(function(data) {
            console.log(data);
            return data
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
};


function compare(user_id, name, price) {
    fetch(`http://52.54.115.82:8080/compare/${user_id}`, {
        method: "GET",
        headers: {
            'name': name,
            'price': price
        }
    })
    .then(
        function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
            return;
        }
        // Examine the text in the response
        response.json().then(function(data) {
            console.log(data);
            return data
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
};

function get_person(user_id) {
    fetch(`http://52.54.115.82:8080/person/${user_id}`, {method: "GET"})
    .then(
        function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
            return;
        }
        // Examine the text in the response
        response.json().then(function(data) {
            console.log(data);
            return data
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
}

function delete_person(user_id) {
    fetch(`http://52.54.115.82:8080/delete/${user_id}`, {method: "POST"})
    .then(
        function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
            return;
        }
        // Examine the text in the response
        response.json().then(function(data) {
            console.log(data);
            return data
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
}
