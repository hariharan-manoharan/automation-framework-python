demo = {

    initDocumentationCharts: function(pass, fail) {
        var chart = new Chart(document.getElementById("pie-chart"), {
            type: 'doughnut',
            data: {
                labels: ["pass", "fail"],
                datasets: [{
                    label: "Tests view",
                    backgroundColor: ["#66FF66", "#FF3333"],
                    data: [pass, fail],
                    borderColor: "white",
                    borderWidth: 2
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Tests view',
                    responsive: false
                }
            }
        });
    }
}