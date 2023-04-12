

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



  