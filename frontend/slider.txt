'use strict';
const noUiSlider = require('nouislider');

class Slider {
  // constructs sliders using noUiSlider
  constructor(el, image){
    this.slider = el;
    this.image = image;
    this.imageInfo = this.getImageInfo();
    this.scale = this.getScale();
  }

  create() {
    // Sets slider configuration based on imageInfo.  Sets slider action
    // to switch to the image in the series corresponding to the slider's
    // position.  Sets slider width or height to the dimension of the
    // corresponding image.
    const orient = this.image.height > this.image.width ? 'vertical' : 'horizontal';
    noUiSlider.create(this.slider, {
      start: this.imageInfo.first,
      connect: 'lower',
      orientation: orient,
      tooltips: true,
      step: 1,
      range: {
        min: this.imageInfo.first,
        max: this.scale.max
      },
      pips: {
        mode: 'values',
        values: this.scale.steps,
        stepped: false,
        density: 4
      },
      format: {
        to: value =>  Math.floor(Number(value)), // format number in tooltips to integer
        from: value => Math.floor(Number(value))
      }
    });

    this.slider.noUiSlider.on('slide', () => {
      const value = this.slider.noUiSlider.get();
      this.switchToImage(value);
    });
    if (orient === 'horizontal') {
      this.slider.style.width = this.image.width + 'px';
    } else {
      this.slider.style.height = this.image.height + 'px';
    }
  }


  getImageInfo() {
    // returns object with data about this.image for use in building sliders
    // {
    //   first: number of first image in collection
    //   filenameLength: length of filenames in collection.  currently passed from backend as 6 digits with leaing zeroes
    //   extension: file extension
    //  _dir: path to image file
    // }
    const imageInfo = {};
    const path = this.image.getAttribute('src');
    const pathArr = path.split('/');
    imageInfo.first = Number( pathArr.slice(-1)[0].split('.')[0] );
    imageInfo.filenameLength = pathArr.slice(-1)[0].split('.')[0].length;
    imageInfo.extension = '.' + pathArr.slice(-1)[0].split('.').slice(-1)[0];
    imageInfo._dir = pathArr.slice(0, pathArr.length - 1).join('/') + '/';
    return imageInfo;
  }

  getScale() {
    // Returns data for slider scale.  Series length data stored as data
    // atribute of a div with id 'data-store.'
    const zMax = Number( document.querySelector('#data-store').getAttribute(`data-${this.image.id}`) ) - 1;
    const scaleSteps = [];
    for ( var i = 0; i <= zMax; i += ~~(zMax / 10) ) {
      scaleSteps.push(i);
    }
    if ( zMax - scaleSteps.slice(-1)[0] < ~~(zMax / 10) ) {
      scaleSteps.pop();
    }
    scaleSteps.push(zMax);
    return { max: zMax, steps: scaleSteps };
  }

  switchToImage(idx) {
    // Takes an index and switches the 'src' attribute of the slider's
    // image element to match the png file corresponding to that index in the series
    idx = idx.toString();
    const leadingZeroes = this.imageInfo.filenameLength - idx.length;
    for (var i = 0; i < leadingZeroes; i++) {
      idx = '0' + idx;
    }
    const newSrc = this.imageInfo._dir + idx + this.imageInfo.extension;
    this.image.src = newSrc;
  }
}

module.exports = Slider;
