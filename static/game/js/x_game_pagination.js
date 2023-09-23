let infScroll = new InfiniteScroll( '.infinity-container', {
  path: '.infinite-more-link',
  append: '.infinity-post',
  button: '.view-more-button',
  scrollThreshold: false,
  status: '.page-load-status',
  checkLastPage: true,
  history: false,
});
