document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("search-form");
    const resultsDiv = document.getElementById("results");
    const chartDiv = document.getElementById("chart");

    searchForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const query = document.getElementById("query").value;

        fetch("/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `query=${encodeURIComponent(query)}`,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response error");
                }
                return response.json();
            })
            .then((data) => {
                displayResults(data);
                plotChart(data);
            })
            .catch((error) => {
                resultsDiv.innerHTML = `<p class="error">An error occurred: ${error.message}</p>`;
                console.error("Error:", error);
            });
    });

    function displayResults(data) {
        resultsDiv.innerHTML = "";
        data.forEach((result) => {
            const resultDiv = document.createElement("div");
            resultDiv.classList.add("result");
            resultDiv.innerHTML = `
                <h3>Document ${result.doc_id}</h3>
                <p>${result.content}</p>
                <p><strong>Similarity:</strong> ${result.similarity}</p>
            `;
            resultsDiv.appendChild(resultDiv);
        });
    }

    function plotChart(data) {
        const docIds = data.map((result) => `Doc ${result.doc_id}`);
        const similarities = data.map((result) => result.similarity);

        const trace = {
            x: docIds,
            y: similarities,
            type: "bar",
            marker: {
                color: "rgba(100, 200, 255, 0.6)",
                line: {
                    color: "rgba(100, 200, 255, 1.0)",
                    width: 2,
                },
            },
        };

        const layout = {
            title: "Cosine Similarity of Top Documents",
            xaxis: { title: "Document ID" },
            yaxis: { title: "Cosine Similarity" },
        };

        Plotly.newPlot(chartDiv, [trace], layout);
    }
});