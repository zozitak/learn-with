fetch('https://catfact.ninja/fact')
  .then((response) => response.json())
  .then((data) => {
    var text = JSON.stringify((data)['fact'])
    document.getElementById('egy').innerHTML = text;
  });