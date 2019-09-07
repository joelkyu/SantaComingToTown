// this javascript file will be called as a content script from the manifest.json file. the content script will only be called on an amazon shop page.


//Find Item Names
var itemNames = document.getElementsByClassName("a-size-base-plus a-color-base a-text-normal");

for (i=0; i < itemNames.length; i++) {
    console.log(itemNames[i].textContent);
};

// Find Item Prices
var itemPricesWhole = document.getElementsByClassName("a-price-whole");
var itemPricesFraction = document.getElementsByClassName("a-price-fraction");

for (i=0; i< itemPricesWhole.length; i++) {
    console.log([itemPricesWhole[i].textContent + itemPricesFraction[i].textContent])
};
