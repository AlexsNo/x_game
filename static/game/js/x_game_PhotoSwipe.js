import PhotoSwipeLightbox from '/static/game/js/photoswipe-lightbox.esm.js';

const lightbox = new PhotoSwipeLightbox({
  gallery: '#my-gallery',
  children: 'a',
  pswpModule: () => import('/static/game/js/photoswipe.esm.js'),
});

lightbox.init();


