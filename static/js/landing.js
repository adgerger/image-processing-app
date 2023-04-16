
document.getElementById("upload-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    console.log("Post request is being made from the landing.js");
    // Create a FormData object from the form
    const formData = new FormData(event.target);

    // Send a POST request to the Flask server using Fetch API
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }

        const result = await response.text();
        console.log(result);

        // Handle the response, e.g., reload the page or display a success message
        // window.location.reload();
    } catch (error) {
        console.error('Error:', error);
    }
});


