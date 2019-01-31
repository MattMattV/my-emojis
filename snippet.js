// Credits to JPablomr (https://gist.github.com/itsrachelle/0a139a3f53d36b5b24359bcc99b39b3a#gistcomment-2696592)

// Helper
// sleep time expects milliseconds
function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}


// Create a Map where we're going to store all of the images.
var imgContainer = new Map();
var t = $('div.c-virtual_list__scroll_container')[0];
// Populate items present on the page at start
for (imgEl of $('img.p-customize_emoji_list__image')) {
    imgContainer.set(imgEl.alt, imgEl);
}
t.addEventListener("DOMNodeInserted", function (event) {
    el = event.target;
    imgElResults = $(el).find('img.p-customize_emoji_list__image');
    if (imgElResults.length) {
        imgEl = imgElResults[0];
        if (!imgContainer.has(imgEl.alt)) {
            imgContainer.set(imgEl.alt, imgEl);
        }
    }
}, false);

// Now scroll to the bottom and then to the top so that list populates.
// Track the inside container's position
var scrollPosition = $('.c-scrollbar__hider')[0].scrollTop;
// Bump this higher if it's stopping mid-list.
var SLEEP_TIME = 750;

while (true) {
    // We're not sure how big the container is as it's loaded dynamically
    // So we scroll in increments of 500
    var newScrollPosition = $('.c-scrollbar__hider')[0].scrollTop += 500;
    // We know we've hit the bottom when the position stops changing
    if (newScrollPosition == scrollPosition) {
        break;
    }
    // Otherwise let's track the current position and keep going
    scrollPosition = newScrollPosition;
    // Sleep so the page can load the new emojis
    await sleep(SLEEP_TIME);
}

// Create the Array from the imgContainer map
var emojiArr = ['[\n'];
var emojiIndex = 0;
imgContainer.forEach(function (value, key, map) {
    var url = value.src;
    var extension = url.substring(url.lastIndexOf('.')); // key is name
    emojiArr.push(JSON.stringify({ name: key, extension: extension, url: url }) + (++emojiIndex < map.size ? ',\n' : '\n]'));
});
console.log(emojiArr.join(''));