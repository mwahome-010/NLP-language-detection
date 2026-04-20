async function predict() {
    const text = document.getElementById("text").value;
    const model = document.getElementById("model").value;

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text, model: model })
    });

    const data = await response.json();

    let html = data.input + "<br><br>";

    if (data.result.svm) {
        html += "<b>SVM:</b> " + data.result.svm.prediction;
        
        html += "<br>";
    }

    if (data.result.nb) {
        html += "<b>Naive Bayes:</b> " + data.result.nb.prediction;
       
    }

    document.getElementById("output").innerHTML = html;
}