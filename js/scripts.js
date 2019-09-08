// this javascript file will be called as a content script from the manifest.json file. the content script will only be called on an amazon shop page.

// IIFE that returns an array of objects with Amazon item names and prices
(function () {
    var itemNames = document.getElementsByClassName("a-size-base-plus a-color-base a-text-normal");
    var itemPricesWhole = document.getElementsByClassName("a-price-whole");
    var itemPricesFraction = document.getElementsByClassName("a-price-fraction");

    var itemArray = []

    for (i=0; i<itemNames.length; i++) {
        itemArray.push({name: itemNames[i].textContent, price: parseFloat(itemPricesWhole[i].textContent + itemPricesFraction[i].textContent)});
    };

    console.log(itemArray);

    return itemArray;

})();
