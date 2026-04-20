const fs = require('fs');
const html = fs.readFileSync('tmp_form.html', 'utf-8');
const match = html.match(/var FB_PUBLIC_LOAD_DATA_ = (.*?);<\/script>/s);
if(match) {
    const data = JSON.parse(match[1]);
    const questions = data[1][1];
    questions.forEach(q => {
        try {
            console.log("Title: " + q[1] + ", ID: entry." + q[4][0][0]);
        } catch(e) {}
    });
}
