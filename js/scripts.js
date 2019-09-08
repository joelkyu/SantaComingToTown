// this javascript file will be called as a content script from the manifest.json file. the content script will only be called on an amazon shop page.

// IIFE that returns an array of objects with Amazon item names and prices
// (function () {
//     let item = document.getElementsByClassName("a-size-base-plus a-color-base a-text-normal");
//     let itemPricesWhole = document.getElementsByClassName("a-price-whole");
//     let itemPricesFraction = document.getElementsByClassName("a-price-fraction");
//
//     let items = {}
//
//     for (i=0; i<item.length; i++) {
//         item.setAttribute('id', i);
//         for (i=1; i<=localStorage.getItem('max_id'); i++) {
//             fetch(`http://52.54.115.82:8080/compare/${user_id}`, {
//                 method: "GET",
//                 headers: {
//                     "accept": 'application/json',
//                     'name': itemNames[i].textContent,
//                     'price': parseFloat(itemPricesWhole[i].textContent + itemPricesFraction[i].textContent)
//                 }
//             })
//             .then(
//                 function(response) {
//                 if (response.status !== 200) {
//                     console.log('Looks like there was a problem. Status Code: ' +
//                     response.status);
//                     return;
//                 }
//                 // Examine the text in the response
//                 response.json().then(function(data) {
//                     console.log(data);
//                     return data
//                 });
//                 }
//             )
//         }
//
//     };
// })();

(function () {
    var itemNames = document.getElementsByClassName("a-size-base-plus a-color-base a-text-normal");
    var itemPricesWhole = document.getElementsByClassName("a-price-whole");
    var itemPricesFraction = document.getElementsByClassName("a-price-fraction");

    var ids = [];
    var names = [];
    var prices = [];

    for (i=0; i<itemNames.length; i++) {
        $(itemNames[i]).attr('id', i);
        try {
            names.push(itemNames[i].textContent)
            prices.push(parseFloat(itemPricesWhole[i].textContent + itemPricesFraction[i].textContent));
            ids.push(i);
        }
        catch(err) {
            console.log(err);
        }
    };

    localStorage.setItem('names', names);
    localStorage.setItem('ids', ids);
    localStorage.setItem('prices', prices);
    console.log('done!')
})();
