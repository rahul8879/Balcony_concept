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

   // Function to show the "Thank you" popup
    // function showThankYouPopup() {
    //   console.log('Show thank you popup called');
    //   var popup = document.createElement("div");
    //   popup.innerHTML = "Thank you";
    //   // Add any desired styles to the popup element
    //   document.body.appendChild(popup);
    //   setTimeout(function() {
    //     document.body.removeChild(popup);
    //   }, 5000); // Remove the popup after 5 seconds
    // }

     // Function to show the second modal (thank you popup)
       // Function to show the second modal (thank you popup) with response message
      function showThankYouPopup(responseMessage) {
        $('#thankYouModal .thank-you-text').text(responseMessage);
        $('.thank-you-modal').fadeIn();
        setTimeout(function() {
          hideThankYouPopup();
        }, 5000); // Automatically hide the second modal after 5 seconds
      }

       // Function to hide the second modal (thank you popup)
      function hideThankYouPopup() {
        $('.thank-you-modal').fadeOut();
      }

    // Function to handle form submission
    function handleSubmit(event) {
      event.preventDefault();
      var form = event.target;
      // Send the form data to your Django API using fetch
      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
      })
        .then(function(response) {
          return response.json(); // Parse response as JSON
        })
        .then(function(data) {
          console.log('API Response:', data); // Log the API response for debugging
          if (data.status === "success") {
            console.log('data.message: ',data.message)
            showThankYouPopup(data.message);
            // Hide the modal after successful submission
            $('.modal').fadeOut();
          } else {
            console.log('API Error:', data.message); // Log the error message if needed
          }
        })
        .catch(function(error) {
          console.log('Error:', error);
        });
    }

    // Add event listener to submit the form
    $('#quote-form').submit(handleSubmit);


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

 $(document).ready(function () {
        console.log('JS working')
        $("#bookingForm").submit(function (event) {
            event.preventDefault(); // Prevent form submission to the server

            // Show the loader
            $(".loader").show();

            // Get form data
            var formData = $(this).serialize();

            // Get the slug from the URL
            var url = window.location.href; // Get the complete URL
            console.log('url:', url)
            var slugIndex = url.lastIndexOf('/') + 1; // Find the last occurrence of "/"
            var slug = url.slice(slugIndex); // Extract the slug from the URL

            // Append the slug to the URL
            var submitUrl = url + "submit_booking"+"?" + formData  ; // Replace with the actual URL to your Django view
            console.log('submitUrl:', submitUrl)
            // AJAX form submission
            $.ajax({
                type: "GET",
                url: submitUrl,
                data: formData,
                success: function (response) {
                    // Hide the loader
                    $(".loader").hide();

                    // Show the confirmation message
                    $(".confirmation-message").html(response.message).show();

                    // Clear the form data
                    $("#bookingForm")[0].reset();

                    // Log success message
                    console.log("Form submitted successfully! Response:", response);
                },
                error: function (xhr, status, error) {
                    // Hide the loader
                    $(".loader").hide();

                    // Log error message
                    console.log("Form submission encountered an error! Status:", status);
                    console.log("Error:", error);
                }
            });

            // Log form submitted
            console.log("Form submitted.");
        });
    });

 function openWhatsApp() {
            const phoneNumber = "9821512725"; // Replace with your WhatsApp number
            const preText = "I want to know about the product"; // Replace with your pre-text message
            const url = `https://api.whatsapp.com/send?phone=${phoneNumber}&text=${encodeURIComponent(preText)}`;
            window.open(url);
 }