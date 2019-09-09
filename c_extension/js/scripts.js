// this javascript file will be called as a content script from the manifest.json file. the content script will only be called on an amazon shop page.

var itemNames = document.getElementsByClassName("a-size-base-plus a-color-base a-text-normal");
var itemPricesWhole = document.getElementsByClassName("a-price-whole");
var itemPricesFraction = document.getElementsByClassName("a-price-fraction");

var ids = [];
var names = [];
var prices = [];

for (i = 0; i < itemNames.length; i++) {
    $(itemNames[i]).attr('id', i);
    try {
        names.push(itemNames[i].textContent)
        prices.push(parseFloat(itemPricesWhole[i].textContent + itemPricesFraction[i].textContent));
        ids.push(i);
    }
    catch (err) {
        console.log(err);
    }
};


