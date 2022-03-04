let load = function(url, callback) {
  let ajax = new XMLHttpRequest();
  ajax.open('GET', url);
  ajax.onload = function() {
    callback(this.responseText);
  };
  ajax.send();
};

load('text.txt', function(data) {
  console.log(data);
});
