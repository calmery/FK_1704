(function (jQuery) {
    jQuery(function () {
 
        jQuery('.button-collapse').sideNav();
        $('.dropdown-button').dropdown({
            constrain_width: false,
            hover: true,
            belowOrigin: true
        });
        
        $('.parallax').parallax();
        $('.slider').slider({
            indicators: true,
            height: 300,
            transition: 1000,
            interval: 3000
        });
 
    });
})(jQuery);