async function predict() {
    const text = document.getElementById("text").value;
    const model = document.getElementById("model").value;

    if (!text.trim()) {
        document.getElementById("output").innerHTML = "<span style='color: red; font-size: 24px; text-align: center;'>Please enter some text !.</span>";
        return;
    }

    if (!isNaN(text)) {
        document.getElementById("output").innerHTML = "<span style='color: red; font-size: 24px; text-align: center;'>Please enter valid text !.</span>";
        return;
    }

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