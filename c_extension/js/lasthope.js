setTimeout(function() {
    console.log(results);
    for (i=0; i<results.length; i++) {
        let color;
        if (results[i].score <= 0.5) {
            color = '#4dff4d';
            document.getElementById(results[i].id).setAttribute('style', 'background-color: #4DFF4D')
        }
    }}, 20000)

console.log('Done! Highlighting!')
