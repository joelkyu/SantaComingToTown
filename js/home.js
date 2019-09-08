var results = []

for (i=0; i<ids.length; i++) {
    fetch(`http://52.54.115.82:8080/compare/${ids[i]}`, {
        method: "GET",
        headers: {
            "accept": 'application/json',
            'name': names[i],
            'price': prices[i]
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
            var score = 0
            for(var propName in data) {
                if(data.hasOwnProperty(propName)) {
                    var propValue = data[propName];
                    score = propValue
                }
            }
            results.push({
                id: ids[i],
                score: score
            })
        });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
}
