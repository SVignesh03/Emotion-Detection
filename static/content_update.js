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

function updateContent() {
    $.ajax({
        url: '/get_content', // Replace with your endpoint URL to fetch updated data
        method: 'GET',
        success: function (response) {
            // Update the content dynamically
            $('#top-emotion').text(response.top_emotion);
            $('#emotion-image').attr('src', response.image_url);
            $('#captured-img').attr('src', response.img_url + '?timestamp=' + new Date().getTime());
        }
    });
}

function updateGif() {
    $.ajax({
        url: '/gif', // Replace with your endpoint URL to fetch updated data
        method: 'GET',
        success: function (response) {
            // Update the content dynamically
            // $('#top-emotion').text(response.top_emotion);
            $('#emotion-image').attr('src', response.image_url);
            // $('#captured-img').attr('src', response.img_url + '?timestamp=' + new Date().getTime());
        }
    });
}

$(document).ready(function () {
    setTimeout(updateContent, 5000);
    setInterval(updateContent, 15000);
    setTimeout(updateGif, 10000);
    setInterval(updateGif, 15000);
});

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