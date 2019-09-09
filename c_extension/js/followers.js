// fetch(`http://52.54.115.82:8080`, {method: "GET",}).then(
//     function(response) {
//     if (response.status !== 200) {
//         console.log('Looks like there was a problem. Status Code: ' + response.status);
//         return;
//     }
//     // Examine the text in the response
//     console.log(response);
//     response.json().then(function(data) {
//         for (let person of data) {
//             let name = document.createElement('p');
//             name.textContent = person.twitter;
//             name.setAttribute('class', 'name');
//
//             let price = document.createElement('span');
//             price.setAttribute('class', 'price');
//             price.textContent = '$' + person.lower_price + ' - ' + '$' + person.upper_price;
//
//             let row = document.createElement('li');
//             row.appendChild(name);
//             row.appendChild(price);
//             document.appendChild(row);
//         };
//     }
// );
// .catch(function(err) {
//     console.log('Fetch Error :-S', err);
// });

fetch(`http://52.54.115.82:8080`, {method: "GET",})
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

        data.map((item, idex) => {
            let name = document.createElement('p');
            name.textContent = item.twitter;
            name.setAttribute('class', 'name');

            let price = document.createElement('span');
            price.setAttribute('class', 'price');
            price.textContent = '$' + item.lower_price + ' - ' + '$' + item.upper_price;

            let row = document.createElement('li');
            row.appendChild(name);
            row.appendChild(price);
            document.getElementById('followers_list').appendChild(row);

        localStorage.setItem('max_id', data.length);

        })
    });
    }
)
.catch(function(err) {
    console.log('Fetch Error :-S', err);
});
