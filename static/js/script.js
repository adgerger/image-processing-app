
window.onload = function() {

    /* Get all the popups, operation buttons and close buttons in the document. */
    const allPopups = document.querySelectorAll('.popup-container');
    const allButtons = document.querySelectorAll(".operation-button");
    const closeButtons = document.querySelectorAll('.close-button');
    
    /* Make it so that every operation button opens up it's respective popup when clicked. */
    allButtons.forEach(function(element, index) {
        element.addEventListener('click', () => {
            allPopups[index].style.display = 'flex';
        });
    });

    /* Add closing functionality that makes sure every popup is closed when clicked, for each close button. */
    closeButtons.forEach(button => {
        button.addEventListener('click', () => { 
            allPopups.forEach(popup => {
            popup.style.display = 'none';
            })
        });
    });

    
    /* Functions for all POST requests to the backend */
    
    function displayInfoHandler() {
        console.log("displayInfoHandler invoked on javascript.");
    
        fetch('/displayImageInfo', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        })
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.error(error));
      }
    
    
    function cropHandler() {
        console.log("cropHandler invoked on javascript.");
    
        fetch('/cropImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
      
    function flipHandler() {
        console.log("flipHandler invoked on javascript.");
    
        fetch('/flipImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function scaleHandler() {
        console.log("displayInfoHandler invoked on javascript.");
    
        fetch('/scaleImage', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        })
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.error(error));
      }
      
    
    function rotateHandler() {
        console.log("rotateHandler invoked on javascript.");
    
        fetch('/rotateImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function linearMapHandler() {
        console.log("linearMapHandler invoked on javascript.");
    
        fetch('/linearMapImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function powerLawMapHandler() {
        console.log("powerLawMapHandler invoked on javascript.");
    
        fetch('/powerLawMapImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function histogramHandler() {
        console.log("histogramHandler invoked on javascript.");
    
        fetch('/calculateHistogram', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function equalizeHistogramHandler() {
        console.log("equalizeHistogramHandler invoked on javascript.");
    
        fetch('/histogramEqualizeImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function convolutionHandler() {
        console.log("convolutionHandler invoked on javascript.");
    
        fetch('/convoluteImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }
    
    
    function nonLinearFilterHandler() {
        console.log("nonLinearFilterHandler invoked on javascript.");
    
        fetch('/filterImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            }
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }

};




  