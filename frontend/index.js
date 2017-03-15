'use strict'
const Slider = require('./slider');

//entrypoint
document.addEventListener('DOMContentLoaded', () => {
  renderPageElements();
});

function renderPageElements() {
  // Creates new slider for each div in the DOM with class name 'slider'
  // and passes it a reference to the image element that it will modify.
  const sliders = document.querySelectorAll('.slider');
  for (var i = 0; i < sliders.length; i++) {
    const img = document.querySelector('#' + sliders[i].id[0]);
    const slider = new Slider(sliders[i], img);
    setTimeout( () => slider.create(), 100 );
  }
}
