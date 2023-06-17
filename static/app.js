// let refreshIntervalId
function stop() {
    $.ajax({
        url: "/stop",
        method: "POST",
        success: function (response) {
            console.log(response);
            // Redirect to the stop page
            window.location.href = "/stop";
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function start() {
    $.ajax({
        url: "/start_page",
        method: "POST",
        success: function (response) {
            console.log(response);
            // Redirect to the start page
            window.location.href = "/start_page";
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function pause() {
    $.ajax({
        url: "/pause",
        method: "POST",
        success: function (response) {
            console.log(response);
            // Redirect to the pause page
            window.location.href = "/pause_page";
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function play() {
    $.ajax({
        url: "/play",
        method: "POST",
        success: function (response) {
            console.log(response);
            // Redirect to the start page
            window.location.href = "/start_page";
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function home() {
    $.ajax({
        url: "/home",
        method: "POST",
        success: function (response) {
            console.log(response);
            // Redirect to the start page
            window.location.href = "/home_page";
        },
        error: function (error) {
            console.log(error);
        }
    });
}


function kill() {
    alert('Server shutting down...');
    fetch('/quit', {
        method: 'POST'
    })
        .then(response => {
            if (response.ok) {
                alert('Server shutting down...');
            } else {
                alert('Failed to shut down the server.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}