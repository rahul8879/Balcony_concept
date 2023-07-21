$(document).ready(function() {
    // Explicitly hide the modal on page load
    $('.modal').hide();

    // Close the modal when the user clicks outside the form or the close button
    $('.modal, .close').click(function(event) {
        if ($(event.target).hasClass('modal') || $(event.target).hasClass('close')) {
            $('.modal').fadeOut();
            console.log('Modal hidden.');
        }
    });

    // Show the modal when the "Get Quote" button is clicked
    $('.round-btn').click(function(event) {
        event.preventDefault(); // Prevent default anchor tag behavior (e.g., navigation)

        // Show the modal
        $('.modal').fadeIn();
        console.log('Modal shown.');
    });
});

 if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    var latitude = position.coords.latitude;
                    var longitude = position.coords.longitude;

                    // Send the latitude and longitude to the Django view using Fetch API
                    fetch("{% url 'capture_location' %}", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": "{{ csrf_token }}",  // Include the CSRF token for security
                        },
                        body: JSON.stringify({  // Send the data as JSON in the request body
                            latitude: latitude,
                            longitude: longitude,
                        }),
                    });
                },
                function(error) {
                    // Handle error if geolocation is not available or user denies the request
                }
            );
        }