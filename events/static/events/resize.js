// sets height of carousel

// Normalize Carousel Heights - pass in Bootstrap Carousel items.
function normalizeSlideHeights() {
    $('.carousel').each(function(){
      var items = $('.carousel-item', this);
      // reset the height
      items.css('min-height', 0);
      // set the height
      var minHeight = Math.min.apply(null,
          items.map(function(){
              return $(this).outerHeight()}).get());
      items.css('max-height', minHeight+'px');
    })
}

$(window).on(
    'load resize orientationchange',
    normalizeSlideHeights);
