(function(fn) {
	'use strict';
	fn(window.jQuery, window, document);
}(function($, window, document) {
	'use strict';
	
	$(function() {
		$('.sort-direction').on('click', '[data-sort]', function(event) {
			event.preventDefault();
			
			let $this = $(this),
				sortDir = 'desc',
                d = 'M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708z',
                title = ' по убыванию';
                
            if ($this.data('sort') !== 'asc') {
                sortDir = 'asc';
                d = 'M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708';
                title = ' по возрастанию';
            }
			
            $this.attr('title', title).data('sort', sortDir).find('.bi').find('path').attr('d', d);
			
			// call sortDesc() or sortAsc() or what have you...
		});
	});

}));