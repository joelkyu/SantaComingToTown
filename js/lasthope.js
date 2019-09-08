[{id: 1, score: 0.2}, {id: 2, score: 0.5}, {id: 3, score: 1}]


for (i=0; i<results.length; i++) {
    let color = '';
    if (results[i].score >= 0.5) {
        color = '#4dff4d';
        document.getElementById(results[i].id).setAttribute('style', 'background-color: #4DFF4D')
    }
}
