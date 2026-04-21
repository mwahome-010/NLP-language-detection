async function predict() {
    const text = document.getElementById("text").value;
    const model = document.getElementById("model").value;

    if (!text.trim()) {
        document.getElementById("output").innerHTML = "<span style='color: red; font-size: 24px; text-align: center;'>Please enter some text !.</span>";
        return;
    }

    if (!isNaN(Number(text)) && text.trim() !== "") {
        document.getElementById("output").innerHTML = "<span style='color: red; font-size: 24px; text-align: center;'>Please enter valid text !.</span>";
        return;
    }

    let data;
    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text, model: model })
        });
        data = await response.json();

        function escapeHTML(str) {
            return String(str)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#39;");
        }

        let html = "<br>";

        if (data.result && data.result.svm) {
            html += "<b>SVM:</b> " + escapeHTML(data.result.svm.prediction);
            html += "<br>";
            html += "<br>";
        }

        if (data.result && data.result.nb) {
            html += "<b>Naive Bayes:</b> " + escapeHTML(data.result.nb.prediction);
        }

        document.getElementById("output").innerHTML = html;
    } catch (error) {
        document.getElementById("output").innerHTML = "<span style='color: red; font-size: 24px; text-align: center;'>An error occurred while predicting.</span>";
    }
}