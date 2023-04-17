
window.onload = function() {

    /* Get all the popups, operation buttons and close buttons in the document. */
    const allPopups = document.querySelectorAll('.popup-container');
    const allButtons = document.querySelectorAll(".operation-button");
    const closeButtons = document.querySelectorAll('.close-button');
    
    /* Make it so that every operation button opens up it's respective popup when clicked. */
    allButtons.forEach(function(element, index) {
        element.addEventListener('click', () => {
            if (element.id == 'displayInfoButton') {
              displayInfoHandler();
            }
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
        .then(result => {

          document.getElementById('imageSizePlaceholder').textContent = '1024 x 768';
          document.getElementById('numPixelsPlaceholder').textContent = '786,432';
          document.getElementById('imageTypePlaceholder').textContent = result;
          document.getElementById('colorPlaceholder').textContent = 'RGB';

        })
        .catch(error => console.error(error));
      }
    
    
    function cropHandler() {
        console.log("cropHandler invoked on javascript.");
    
        fetch('/cropImage', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify({ data: 'lol' })
          })
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.error(error));
    
      }

    

};


function histogramHandler() {
  console.log("histogramHandler invoked on javascript.");

  fetch('/calculateHistogram', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      }
    })
    .then(response => response.text())
    .then(result => {console.log(result); window.location.reload();})
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
    .then(result => {
      console.log(result);
      
      window.location.reload();

    
    })
    .catch(error => console.error(error));

}   


function nonLinearFilterHandler(event) {
  event.preventDefault();
  
  console.log("nonLinearFilterHandler invoked on javascript.");

  const windowSize = document.getElementById("windowSize").value;
  const typeSelect = document.getElementById("typeSelect").value;

  console.log("Window Size:", windowSize);
  console.log("Type:", typeSelect);

  fetch('/filterImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ window: windowSize, type: typeSelect, color: 'false'})
    })
    .then(response => response.text())
    .then(result => {
      
      console.log(result);
      window.location.reload();
    
    })
    .catch(error => console.error(error));

}
    
function convolutionHandler(event) {
  event.preventDefault(); 

  console.log("convolutionHandler invoked on javascript.");

  const kernel = document.getElementById("kernel").value;
  console.log("kernel:", kernel);

  fetch('/convoluteImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ kernel: kernel, color: 'false' })
    })
    .then(response => response.text())
    .then(result => {
    
      console.log(result)
      window.location.reload()
    
    })
    .catch(error => console.error(error));

}

function powerLawMapHandler(event) {
  event.preventDefault(); 

  console.log("powerLawMapHandler invoked on javascript.");

  const cCoefficient = document.getElementById("cCoefficient").value;
  const gamma = document.getElementById("gamma").value;

  console.log("a:", cCoefficient);
  console.log("b:", gamma);

  fetch('/powerLawMapImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ c: cCoefficient, gamma: gamma })

    })
    .then(response => response.text())
    .then(result => {

      console.log(result)
      window.location.reload()
    
    })
    .catch(error => console.error(error));

}

    
function linearMapHandler(event) {
  event.preventDefault();

  console.log("linearMapHandler invoked on javascript.");

  const aCoefficient = document.getElementById("aCoefficient").value;
  const bCoefficient = document.getElementById("bCoefficient").value;

  console.log("a:", aCoefficient);
  console.log("b:", bCoefficient);


  fetch('/linearMapImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ a: aCoefficient, b: bCoefficient })
    })
    .then(response => response.text())
    .then(result => {
      
      console.log(result);

      window.location.reload()

    })
    .catch(error => console.error(error));

}

    
function rotateHandler(event) {
  event.preventDefault(); 

  console.log("rotateHandler invoked on javascript.");

  const rotationAngle = document.getElementById("rotationAngle").value;

  // Process the input values as needed
  console.log("Output Height:", rotationAngle);



  fetch('/rotateImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ angle: rotationAngle})

    })
    .then(response => response.text())
    .then(result => {
    
      console.log(result);
      window.location.reload()


    })
    .catch(error => console.error(error));
}

function scaleHandler(event) {

  event.preventDefault(); 

  const outputHeight = document.getElementById("outputHeight").value;
  const outputWidth = document.getElementById("outputWidth").value;

  console.log("Output Height:", outputHeight);
  console.log("Output Width:", outputWidth);

  console.log("scaleHandler invoked on javascript.");

  fetch('/scaleImage', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    },
    body: JSON.stringify({ height: outputHeight, width: outputWidth })

  })
  .then(response => response.text())
  .then(result => {
      
      console.log(result);
      window.location.reload();

  })
  .catch(error => console.error(error));

}


function flipHandler(flipType) {
  console.log("flipHandler invoked on javascript.");

  fetch('/flipImage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({ type: flipType })

    })
    .then(response => response.text())
    .then(result => {
      
      console.log(result);
      window.location.reload()

    })
    .catch(error => console.error(error));



}




  