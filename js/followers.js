(function() {
    data = indexPage();
    console.log(data);
    for (person of data) {
        let name = document.createElement('p');
        name.textContent = person.twitter
        name.setAttribute('class', 'name')

        let price = document.createElement('span');
        price.setAttribute('class', 'price')
        price.textContent = `\$${person.lower_price} - \$${person.upper_price}`

        let row = document.createElement('li');
        row.appendChild(name);
        row.appendChild(price);
        document.appendChild(row);
    }
})();
